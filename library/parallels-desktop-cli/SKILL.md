---
name: parallels-desktop-cli
description: Manage Parallels Desktop virtual machines and host virtualization
  settings from macOS using the local Parallels CLI. Use when the agent needs to
  inspect, create, start, stop, configure, snapshot, clone, archive, migrate,
  enter, execute commands in, or troubleshoot Parallels VMs; manage Parallels
  virtual networks, USB routing, licenses, host preferences, or users; work with
  Windows, Linux, macOS, or other guest OS environments on a macOS host; or use
  prlctl, prlsrvctl, prl_disk_tool, prl_convert, prlcore2dmp, or related
  Parallels command-line tools.
---

# Parallels Desktop CLI

Use this skill to operate Parallels Desktop from a macOS terminal. Prefer the local CLI and its installed help over memory or web docs because command availability varies by Parallels version and license edition.

## Required Paths

Call the bundled binaries by absolute path unless `command -v` proves they are on `PATH`:

```bash
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlsrvctl
```

Related Parallels executables in the same directory include `prl_disk_tool`, `prl_convert`, `prlcore2dmp`, `prl_vmarchiver`, `prl_mkiso`, `prl_esd2iso`, `prl_updater_ctl`, and `prl_perf_ctl`. See [references/cli-reference.md](references/cli-reference.md) before using these or when checking full command coverage.

## Operating Rules

1. Start with read-only discovery:
   - `prlctl --help`
   - `prlsrvctl --help`
   - `prlctl list --all --json`
   - `prlctl list -i -f "<ID | NAME>"`
2. Use JSON output when available and parse it instead of scraping tables.
3. Run command-specific help before unfamiliar operations:
   - `prlctl <action> --help`
   - `prlctl set <category> --help`
   - `prlsrvctl <action> --help`
4. Confirm with the user before destructive or disruptive operations, including `delete`, `unregister`, `stop --kill`, `reset`, `snapshot-delete`, `decrypt`, `change-passwd`, license changes, host shutdown, network rewrites, USB reassignment, VM removal, sending diagnostics off the machine, or guest commands that change state. Snapshot switching can discard guest changes; preserve the relevant state and obtain approval before switching.
5. Prefer VM UUIDs for automation. Names are fine for interactive work but can collide or change.
6. Note license limits. Some `prlsrvctl` actions, especially network, USB, and user management, may return "available only in Parallels Desktop for Mac Pro or Business Edition."
7. Do not expose secrets in output. Redact passwords, license keys, activation details, and guest credentials.

## Command Map

Use `prlctl` for VM-level control:

- Miscellaneous: `problem-report`, `guest-debugger`, `debug-dump`
- VM management: `list`, `create`, `delete`, `register`, `unregister`, `clone`, `convert`, `move`, `installtools`, `enter`, `exec`, `send-key-event`, `status`, `capture`, `encrypt`, `decrypt`, `change-passwd`, `archive`, `unarchive`, `protection-set`, `protection-remove`
- Power operations: `start`, `resume`, `pause`, `suspend`, `restart`, `reset`, `reset-uptime`, `stop`
- VM configuration: `set`
- Snapshot management: `snapshot`, `snapshot-delete`, `snapshot-list`, `snapshot-switch`

Use `prlsrvctl` for host and Parallels service control:

- Host/license: `info`, `install-license`, `deferred-license`, `update-license`, `deactivate-license`, `set`, `shutdown`
- Users: `user list`, `user set --def-vm-home`
- Networks: `net info`, `net list`, `net set`
- USB: `usb list`, `usb set`, `usb del`, `usb rename`, `usb cleanup`
- Diagnostics: `problem-report`

For option details, edition notes, and examples, read [references/cli-reference.md](references/cli-reference.md).

## Common Workflows

Inventory:

```bash
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl list --all --json
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl list -i -f "<ID | NAME>"
```

Lifecycle:

```bash
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl status "<ID | NAME>"
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl start "<ID | NAME>"
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl stop "<ID | NAME>"
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl suspend "<ID | NAME>"
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl resume "<ID | NAME>"
```

Snapshots:

```bash
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl snapshot "<ID | NAME>" --name "<name>" --description "<description>"
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl snapshot-list "<ID | NAME>"
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl snapshot-switch "<ID | NAME>" --id <snapshot_uuid>
```

Guest execution requires a running VM and Parallels Tools in the guest. Prefer `--current-user`. Never place real passwords in command arguments, shell history or tool output; if another identity is necessary, require a supported secure credential method and the appropriate authorization:

```bash
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl exec "<ID | NAME>" --current-user <command> [arg...]

```

Configuration uses `set` categories in current Parallels builds, not only flat legacy flags:

```bash
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl set "<ID | NAME>" cpus --help
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl set "<ID | NAME>" memory --help
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlctl set "<ID | NAME>" shared_folders --help
```

Host discovery:

```bash
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlsrvctl info --json
/Applications/Parallels\ Desktop.app/Contents/MacOS/prlsrvctl user list --json
```
