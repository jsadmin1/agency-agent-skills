#!/usr/bin/env python3
"""Stamp a project from a frozen Agent OS V5 master; print a Herdr plan.

Dry-run by default. `stamp --apply` is the only writing path. Nothing here
launches an agent, creates a Herdr session, initializes Git or installs software.
"""
import argparse
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

SLUG = re.compile(r'^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$')
SKIP = {'.git', '.ok', '.DS_Store', '__pycache__'}


class Stop(Exception):
    pass


def require(ok, msg):
    if not ok:
        raise Stop(msg)


def no_symlink_components(path):
    """Refuse a path whose existing components are symlinks (escape risk)."""
    absolute = Path(os.path.abspath(path))
    for part in [absolute, *absolute.parents]:
        if part.exists() or part.is_symlink():
            require(not part.is_symlink(), 'Symlink in path: ' + str(part))
    return absolute


def read_master(source):
    source = no_symlink_components(source)
    version = source / 'VERSION.json'
    require(version.is_file() and (source / 'workspace.json').is_file()
            and (source / 'AGENTS.md').is_file(), 'Not an Agent OS master: ' + str(source))
    data = json.loads(version.read_text(encoding='utf-8'))
    require(data.get('product') == 'Agent OS' and str(data.get('release', '')).startswith('5.'),
            'Unsupported master release: %r' % data.get('release'))
    for path in source.rglob('*'):
        require(not path.is_symlink(), 'Master contains a symlink: ' + str(path.relative_to(source)))
    require((source / 'agents' / 'co-orchestrator').is_dir(), 'Master lacks agents/co-orchestrator.')
    return source, data


def stamp(args):
    slug = args.slug
    require(SLUG.match(slug), 'Slug must be lowercase kebab-case, 2-64 chars.')
    name = args.name.strip()
    require(name and len(name) <= 80 and '\n' not in name, 'Name must be one line, 1-80 chars.')
    source, version = read_master(args.source)
    dest = no_symlink_components(args.dest)
    require(dest.name == slug, 'Destination folder must be named the slug: ' + slug)
    require(dest.parent.is_dir(), 'Destination parent must already exist.')
    require(not dest.exists() and not dest.is_symlink(), 'Destination exists; refusing to overwrite.')
    require(source != dest and source not in dest.parents and dest not in source.parents,
            'Source and destination must not nest.')
    session = args.session or slug
    require(SLUG.match(session), 'Session name must be lowercase kebab-case.')
    result = {'action': 'stamp', 'apply': args.apply, 'source': str(source),
              'release': version.get('release'), 'dest': str(dest),
              'project': {'name': name, 'slug': slug}, 'session_name': session,
              'unchanged': ['setup.status', 'setup.launch_authorized', 'runtime models/permissions'],
              'next': 'Run python3 -B scripts/verify.py in the new root, then the V5 first-run prompt.'}
    if not args.apply:
        result['note'] = 'dry-run; nothing written'
        return result
    stage = Path(tempfile.mkdtemp(prefix='.bootstrap-stage-', dir=str(dest.parent)))
    try:
        shutil.copytree(str(source), str(stage / 'tree'), ignore=shutil.ignore_patterns(*SKIP))
        ws_path = stage / 'tree' / 'workspace.json'
        ws = json.loads(ws_path.read_text(encoding='utf-8'))
        ws['project']['name'] = name
        ws['project']['slug'] = slug
        ws['runtime']['session_name'] = session
        ws_path.write_text(json.dumps(ws, indent=2) + '\n', encoding='utf-8')
        require(not dest.exists(), 'Destination appeared during staging; refusing.')
        (stage / 'tree').rename(dest)
    finally:
        shutil.rmtree(str(stage), ignore_errors=True)
    result['note'] = 'written'
    return result


def herdr_plan(args):
    root = no_symlink_components(args.root)
    ws_file = root / 'workspace.json'
    require(ws_file.is_file(), 'No workspace.json at root: ' + str(root))
    ws = json.loads(ws_file.read_text(encoding='utf-8'))
    session = ws.get('runtime', {}).get('session_name') or ''
    require(SLUG.match(session), 'workspace.json runtime.session_name is unset or invalid.')
    peer = root / 'agents' / 'co-orchestrator'
    require(peer.is_dir() and not peer.is_symlink(), 'Peer home missing: agents/co-orchestrator')
    mode = ws.get('runtime', {}).get('peer_mode')
    return {'action': 'herdr-plan', 'executes': False, 'session': session, 'peer_mode': mode,
            'main_cwd': str(root), 'peer_cwd': str(peer),
            'read_only_first': ['herdr --version', 'herdr session list',
                                'herdr workspace --help', 'herdr agent start --help'],
            'refuse_if': ['session name already listed and not this project',
                          'peer_mode is unconfigured', 'launch not authorized for this task'],
            'then_per_current_help': ['herdr session attach ' + session,
                                      'workspace create --cwd MAIN --label orchestrator --no-focus',
                                      'workspace create --cwd PEER --label co-orchestrator --no-focus (paired only)',
                                      'agent start ... only after explicit launch approval'],
            'verify_before_handoff': ['session/workspace/pane ids', 'harness and native id',
                                      'model, effort, speed, permissions', 'cwd', 'no duplicate client']}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('stamp')
    s.add_argument('--source', required=True)
    s.add_argument('--dest', required=True)
    s.add_argument('--name', required=True)
    s.add_argument('--slug', required=True)
    s.add_argument('--session')
    s.add_argument('--apply', action='store_true')
    h = sub.add_parser('herdr-plan')
    h.add_argument('--root', required=True)
    a = p.parse_args(argv)
    try:
        out = stamp(a) if a.cmd == 'stamp' else herdr_plan(a)
    except (Stop, OSError, ValueError, KeyError) as e:
        print(json.dumps({'ok': False, 'error': str(e)}))
        return 2
    print(json.dumps(dict(ok=True, **out), indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
