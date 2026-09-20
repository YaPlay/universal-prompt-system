# QA CHECKLIST — v1.0

Status: Final

Use this checklist against real files and real transitions. Keyword presence alone is not evidence of PASS.

## Structural QA

- [ ] Every canonical file exists at the registered path.
- [ ] The canonical path registry contains exactly 35 Mode × Language × Version rows.
- [ ] Every registry row resolves to one existing file; every canonical file resolves to one row.
- [ ] Duplicate tuple/path matches are zero.
- [ ] Metadata matches path: Mode, Language, Prompt Version, Status.
- [ ] Current version selection is exact `Prompt Version: v1.0`; no latest/timestamp/glob tie-breaker is used.
- [ ] Numbering is continuous; no duplicate numbers or titles.
- [ ] Markdown and code fences are balanced.
- [ ] No empty or hollow required sections.
- [ ] Cross-file language section counts and order match the RU Source of Truth for each Mode.

## Startup Flow QA

- [ ] Repository URL by itself starts Startup Flow instead of only describing the repository.
- [ ] `новый`, `новый проект`, `начало`, `старт`, `start`, and `new project` start new-project Startup Flow.
- [ ] Language is explicitly confirmed before Mode confirmation.
- [ ] Mode is explicitly confirmed before Main Router Mode activation.
- [ ] `Auto` only proposes one canonical Mode and never silently activates it.
- [ ] Startup Lock blocks Project ID, Progress, Current Position, project State, Stage 1, Task 1.1, Quest 1.1, and Step 1.1 before Language + Mode confirmation.
- [ ] Mode confirmation shows Language, Mode, short description, and an explicit confirmation question.
- [ ] After Startup Flow, Main Router still validates the exact tuple.
- [ ] The loaded Mode's Start Lock remains active after Startup Lock releases.
- [ ] Valid Resume uses the pinned tuple without forcing new-project Language/Mode selection.
- [ ] RU, EN, FR, ES, and UA preserve the same functional startup order.
- [ ] `Auto` is not counted as an eighth canonical Mode and does not change the 35-tuple registry.

## System and Router QA

- [ ] System layer loads before Mode.
- [ ] Requested Mode equals Loaded Mode.
- [ ] Wrong Router target stops with Recovery/Fallback.
- [ ] The complete Core lock inventory is enforced: System Layer Lock, Mode Entry Lock, Mode Heartbeat, Mode Recovery, Command Namespace Lock, Task Scope Lock, Persistent Interface Lock, Project Layer Isolation, Prompt / Artifact Isolation, Old Context Isolation, State Source Priority, Version Pinning, no silent upgrade, no silent downgrade, Single State, and Reality First.
- [ ] Mode, Language, and Version are protected and pinned.
- [ ] Foreign-mode command is rejected by Command Namespace Lock.
- [ ] Task Scope Lock prevents views, questions, Settings, Plan, diagnostics, Export, and resource screens from changing the active Task/Quest/Step.
- [ ] Task Scope Lock maps Task semantics to Standard/Cyber/Executive/Study/Anime Magic, Quest semantics to RPG, and Step semantics to Sakura.
- [ ] Ambiguous current scope opens Recovery instead of guessing.
- [ ] Persistent Interface Lock preserves the loaded Mode's canonical command surface across context actions and localized labels.
- [ ] Tone, Detail, View, and theme settings do not change command semantics.
- [ ] Persistent Interface Lock permits omission only on explicitly exempt raw Export/artifact/code screens.
- [ ] Scope or interface conflicts open Mode Recovery/Recovery and do not silently normalize.
- [ ] Mode UI cannot override Core Locks.
- [ ] Old context cannot contaminate current State.
- [ ] Prompt text and artifacts remain isolated from project State.
- [ ] State Source Priority is applied in conflicts.

## Project-State regression QA

- [ ] Start Lock blocks Project ID, Progress, Current Position, and active State before confirmation.
- [ ] One active Project ID and one Single State are maintained.
- [ ] Task/Quest/Step Lock blocks illegal jumps.
- [ ] Completion, Skip, Cancel, and Reopen preserve status and history.
- [ ] Fake completion and fake progress are rejected.
- [ ] Conflicting Checkpoints open Recovery.
- [ ] Stale Export is not treated as current without confirmation.
- [ ] Damaged/incomplete Export reports missing fields and does not guess.
- [ ] Project Copy creates a new project; Project Export preserves the same project.
- [ ] Resume restores the same Project ID and pinned tuple without a new Start.
- [ ] Final requires validation and separate explicit confirmation.
- [ ] Final → Reopen preserves old Final, reason, history, and Project ID.

## Adversarial QA

- [ ] Wrong Mode in Settings.
- [ ] Wrong Router target.
- [ ] Foreign-mode command.
- [ ] Wrong language file.
- [ ] Wrong version.
- [ ] Stale Export.
- [ ] Damaged Export.
- [ ] Duplicate Project ID.
- [ ] Old-context contamination.
- [ ] Conflicting Checkpoints.
- [ ] Illegal task jump.
- [ ] Fake completion.
- [ ] Fake progress.
- [ ] Mode-specific state leakage.
- [ ] Resume into another Mode.
- [ ] Project Copy / Project Export confusion.
- [ ] Final → Reopen.
- [ ] Language switch mid-project.
- [ ] Version switch mid-project.
- [ ] Cross-mode parity.
- [ ] Cross-language parity.

## Mode-specific QA

- [ ] Standard remains neutral and preserves Project → Stage → Task → Completion and Large + Auto.
- [ ] RPG preserves real-data-only XP, achievements, progress, Map, and Full Map.
- [ ] Sakura remains an adult digital garden with Path/Step semantics and no RPG state.
- [ ] Cyber remains a control center with no fake signals, connections, or diagnostics.
- [ ] Anime Magic remains atmospheric and non-RPG; magic UI cannot create fake State.
- [ ] Executive preserves Decisions, Risks, Metrics, and Action Plan without invented KPI/owner/deadline.
- [ ] Study does not invent understanding, mastery, mistakes, difficulty, or learning progress.

## Result rule

Any real FAIL means the current Quest is `NOT READY`. Only a complete rerun after the last fix may produce a verified result.
