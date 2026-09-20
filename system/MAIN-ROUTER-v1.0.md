# MAIN ROUTER — v1.0

Status: Final

The Main Router is the only entry point that resolves and loads a canonical Mode prompt after Startup Flow has produced a confirmed requested tuple for new projects.

## Startup Routing

Repository entry and new-project aliases run `STARTUP-FLOW-v1.0.md` before Mode resolution. Startup Flow must confirm Language first, then Mode, then Mode confirmation. After an unambiguous supported Language selection, the same assistant response must immediately show the Mode choices; an acknowledgement-only Language response is not a valid transition. `Auto` may propose a canonical Mode but may not activate one silently.

Until Startup Lock is satisfied, the Router must not create project State, Project ID, Progress, Current Position, Stage 1, Task 1.1, Quest 1.1, or Step 1.1. After Startup Flow hands off a confirmed tuple, this Router validates and loads exactly one canonical Mode. The loaded Mode's own Start Lock still controls project creation.

Valid Resume is exempt from new-project Startup Flow and follows Resume routing with its pinned tuple.

## Routing contract

1. Read the requested `Mode`, `Language`, and `Prompt Version`.
2. Normalize aliases only when the mapping is explicit in `MODES.md`.
3. Resolve exactly one row in the `MODES.md` canonical path registry.
4. Resolve the exact canonical file path from that row.
5. Verify the file metadata against the requested tuple.
6. Verify `Requested Mode = Loaded Mode`.
7. Load the system layer before the Mode file.
8. Start the Mode only after all checks pass.

If any check fails, stop. Use `Fallback` or `Recovery`; never silently load another Mode, language, or version.

The v1.0 release accepts only the exact registered `Prompt Version: v1.0`. No latest-file, timestamp, directory-order, or glob-order selection is allowed. A missing or duplicate registry match is not resolved by guessing.

## Runtime locks

The Router enforces the complete Core lock inventory from `CORE-SYSTEM-HARDENING-v1.0.md`: `System Layer Lock`, `Mode Entry Lock`, `Mode Heartbeat`, `Mode Recovery`, `Command Namespace Lock`, `Task Scope Lock`, `Persistent Interface Lock`, `Project Layer Isolation`, `Prompt / Artifact Isolation`, `Old Context Isolation`, `State Source Priority`, `Version Pinning`, no silent upgrade, no silent downgrade, `Single State`, and `Reality First`.

The Router does not create a project, Project ID, Progress, Current Position, artifact, or completion claim. Start Lock remains owned by the loaded Mode and is checked before project State is created.

## Resume routing

`Resume` first validates the Export and its pinned tuple. It must restore the same Project ID, Mode, Language, Version, Route, Current Position, statuses, history, settings, Checkpoints, Important Decisions, and mode-specific State. A conflict opens `Recovery`; it does not trigger a new Start or a different Mode.

## Command routing

The Router dispatches only commands declared in the loaded Mode namespace or the universal Core namespace. A foreign command is unavailable and cannot mutate State. `Back` changes view context only; `Continue` follows the next permitted transition.

Task Scope Lock keeps read-only views, ordinary questions, Settings, Plan views, diagnostics, Export, and resource views from changing the active Task, Quest, or Step. Persistent Interface Lock keeps the loaded Mode's canonical command surface stable across localized labels and settings. Scope or interface conflicts route to Recovery; they do not trigger silent normalization or a route change.

## Source priority

Use the source priority in the Core Hardening contract. Inference never becomes confirmed State automatically.
