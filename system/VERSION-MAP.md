# VERSION MAP — v1.0

Status: Final

## Compatibility contract

The current compatibility tuple is:

`Core System Hardening v1.0` + `Mode` + `Language` + `Prompt Version v1.0`

The seven canonical Modes are Standard, RPG, Sakura, Cyber, Anime Magic, Executive, and Study. Each supports RU, EN, FR, ES, and UA through the exhaustive canonical path registry in `MODES.md` when the exact file exists and its metadata matches.

## Deterministic version selection

The v1.0 release supports exactly `Prompt Version: v1.0`. The Router selects only the single registry row whose Mode, Language, and Prompt Version all match exactly. It must not select a latest file, patch variant, timestamp, directory order, or glob result. A missing row uses `Fallback` or `Recovery`; duplicate rows are a registry conflict and use `Recovery`.

## Pinned-version behavior

- A new project starts only on the exact registered `Prompt Version: v1.0` file for the requested tuple.
- An active project pins its Mode, Language, and Prompt Version.
- `no silent upgrade`: a new prompt version never upgrades an active project silently.
- `no silent downgrade`: a downgrade is never silent.
- A language or Mode change is never silent and never merges two State objects.
- A requested update must show current version, requested version, compatibility, impact, and confirmation actions.
- If the exact tuple is unavailable, use `Fallback`; do not invent a file or silently substitute another tuple.

## Resume compatibility

Resume is compatible only when the Export's pinned Mode, Language, and Version match the requested destination. A mismatch opens `Recovery` and preserves the original tuple until the user chooses a supported action.

## Hardening compatibility

All Mode files are subordinate to `CORE-SYSTEM-HARDENING-v1.0.md`. Mode-specific UI may extend behavior but cannot disable the complete Core lock inventory: System Layer Lock, Mode Entry Lock, Mode Heartbeat, Mode Recovery, Command Namespace Lock, Task Scope Lock, Persistent Interface Lock, Project Layer Isolation, Prompt / Artifact Isolation, Old Context Isolation, State Source Priority, Version Pinning, no silent upgrade, no silent downgrade, Single State, or Reality First.
