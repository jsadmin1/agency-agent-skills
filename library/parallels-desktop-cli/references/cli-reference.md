# Parallels CLI Reference

Examples summarize observed local CLI help; they are version-dependent. On October 13, 2026, `prlctl --version` reported 1.26.4 (23937); `prlsrvctl --version` was unsupported. Recheck each installed command's `--help` before use; this check did not operate a VM.

Documented binaries:

- `/Applications/Parallels Desktop.app/Contents/MacOS/prlctl`
- `/Applications/Parallels Desktop.app/Contents/MacOS/prlsrvctl`

Version note: the original undated capture reported 1.26.3 (23929). The dated check above supersedes it for `prlctl`; no current `prlsrvctl` version was verified.

## `prlctl`

Usage:

```text
prlctl ACTION <ID | NAME> [OPTIONS]
```

Top-level actions:

- Miscellaneous: `problem-report`, `guest-debugger`, `debug-dump`
- VM Management: `list`, `create`, `delete`, `register`, `unregister`, `clone`, `convert`, `move`, `installtools`, `enter`, `exec`, `send-key-event`, `status`, `capture`, `encrypt`, `decrypt`, `change-passwd`, `archive`, `unarchive`, `protection-set`, `protection-remove`
- Power operations: `start`, `resume`, `pause`, `suspend`, `restart`, `reset`, `reset-uptime`, `stop`
- VM Configuration: `set`
- Snapshot Management: `snapshot`, `snapshot-delete`, `snapshot-list`, `snapshot-switch`

Discovery:

```bash
prlctl --help
prlctl <action> --help
prlctl set <category> --help
```

Important action notes:

- `list` supports `--info`, `--all`, `--full`, `--output <fields>`, `--sort`, `--list`, `--template`, `--json`, `--no-header`, `--stopped`, and `--name`.
- `create` supports OS templates, OS type/distribution lists, destination directory, no-HDD creation, custom UUID, and Apple Silicon IPSW restore images.
- `exec` supports `--current-user`, `--user`, `--password`, `--resolve-paths`, and `--use-advanced-terminal`.
- `set` is category-based in this install. Always run category help before changing settings.

`set` categories:

- `cpus`
- `memory`
- `boot`
- `video`
- `mouse`
- `keyboard`
- `printers`
- `usb`
- `bluetooth`
- `startup`
- `optimization`
- `travel`
- `security`
- `smartguard`
- `protection`
- `modality`
- `fullscreen`
- `coherence`
- `timesync`
- `device_mgmt`
- `shared_folders`
- `shared_profiles`
- `shared_apps`
- `smart_mounts`
- `misc_sharing`
- `advanced`
- `misc`
- `network_cond`

Examples:

```bash
prlctl list --all --json
prlctl list -i -f "<ID | NAME>"
prlctl create "<vm_name>" --ostype list
prlctl create "<vm_name>" --distribution list
prlctl status "<ID | NAME>"
prlctl exec "<ID | NAME>" --current-user uname -a
prlctl set "<ID | NAME>" cpus --help
```

## `prlsrvctl`

Usage:

```text
prlsrvctl ACTION [OPTIONS]
```

Global options:

- `--allow-to-confirm`
- `--host-admin <name>`
- `-v,--verbose <number>`

Supported actions and option surface:

```text
info [-j,--json] [--license] [-f,--full]
install-license -k,--key <key> [-n,--name <name>] [-c,--company <name>] [--deferred]
deferred-license <--install | --remove>
update-license
deactivate-license [--skip-network-errors]
set [--mem-limit <auto | size>] [-s,--min-security-level <low | normal | high>]
  [-c,--cep <on | off>]
  [--verbose-log <on | off>]
  [--log-rotation <on | off>]
  [--allow-attach-screenshots <on | off>]
  [--require-pwd <create-vm | add-vm | remove-vm | clone-vm | edit-preferences>:<on | off>]
  [--require-custom-pwd <create-vm | add-vm | remove-vm | clone-vm | edit-preferences>:<on | off>]
  [--custom-pwd [--custom-pwd-mode <on | off | change>] [--replace-commands]]
  [--lock-edit-settings <on | off [--host-admin <name>]>]
  [--host-id <host_id>] [--reset-host-id]
  [--external-dev-auto-connect <host|guest|ask>]
user list [-o,--output <field>[,field...]] [-a,--all] [-H,--no-header] [-s,--sort] [-j,--json]
user set --def-vm-home <path>
net info <vnetwork_id>
net list [-j,--json]
net set <vnetwork_id> [-i,--ifname <if>] [-m,--mac <mac_address>]
  [-t,--type <bridged | host-only | shared>]
  [-d,--description <description>] [-n,--name <new_name>]
  [--ip <ip[/mask]>] [--dhcp-server <on | off>] [--dhcp-ip <ip>]
  [--ip-scope-start <ip>] [--ip-scope-end <ip>]
  [--ip6 <ip[/mask]>] [--dhcp6-server <on | off>] [--dhcp-ip6 <ip>]
  [--ip6-scope-start <ip>] [--ip6-scope-end <ip>]
  [--host-assign-ip6 <on | off>]
  [--connect-host-to-net <on | off>]
  [--nat-<tcp | udp>-add <rule_name,src_port,<dest_ip | dest_vm>,dest_port>]
  [--nat-<tcp | udp>-del <rule_name>] [-j,--json]
usb list [-j,--json] [-c,--compat] [-a,--all]
usb set <<usb-device-id> <vm-uuid | vm-name>> | <--autoconnect <ask | host>> | <--vm <vm-uuid | vm-name>>
usb del <usb-device-id>
usb rename <usb-device-id> <new-name | --auto>
usb cleanup
problem-report <-d,--dump | -s,--send [--proxy [user[:password]@proxyhost[:port]]] | [--no-proxy]>
  [--stand-alone] [--name <user name>] [--email <user E-mail>] [--description <problem_description>]
  [--attach-screenshot <host>] [--detailed] [--no-auto-fallback] [-j,--json]
shutdown [-f,--force]
```

Edition note from live tests:

- `prlsrvctl net list --json`, `prlsrvctl user list --json`, and `prlsrvctl usb list --json` returned: "The command is available only in Parallels Desktop for Mac Pro or Business Edition."

## Related Binaries

The Parallels app bundle also exposes these executable files:

- `prl_client_app`
- `prl_disk_tool`
- `prl_switchspaces`
- `prl_vmarchiver`
- `prl_dmgtool`
- `prl_ps2pdf`
- `prlcore2dmp`
- `prl_packer_inplace`
- `prl_mkiso`
- `prlsrvctl`
- `prlctl`
- `prl_convert`
- `prl_updater_ctl`
- `prl_perf_ctl`
- `prl_esd2iso`
- `prl_macvm_helper`

Use these only after checking their local help or confirming the intended maintenance workflow. Prefer `prlctl` and `prlsrvctl` for normal VM and host management.

## Credential and diagnostic boundaries

Use `--current-user` when suitable. Listed password flags describe syntax only: do not put real credentials in command arguments, shell history or logs. Sending a problem report uploads diagnostics off the machine; inspect and minimize the payload and obtain the required user authorization first. Guest-state changes and snapshot restoration need the same target/backup/approval discipline as host changes.
