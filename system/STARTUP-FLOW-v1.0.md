# STARTUP FLOW — v1.0

Status: Final
Scope: Universal Prompt System pre-routing layer

Startup Flow runs before Main Router Mode activation for repository entry and new-project entry. It never creates project State by itself.

## 1. Purpose

The user must not need to know the repository structure or canonical prompt path. For repository entry or a new-project trigger, use this strict order:

`Repository detected → Startup Flow → Language → Mode → Confirmation → Main Router → Selected Mode → Start Project`

Startup Flow selects a requested tuple. Main Router still owns canonical tuple resolution and Mode loading. The selected Mode still owns its own Start Lock and project creation contract.

## 2. Repository Entry

When the user provides only:

`https://github.com/YaPlay/universal-prompt-system`

recognize Universal Prompt System and start this flow. Do not respond only with a repository description. Do not ask a generic question such as "What do you want to do with this repository?"

The first startup surface must identify Universal Prompt System and request Language. After Language is confirmed, request Mode.

No project, Project ID, Progress, Current Position, task, quest, step, or project State exists yet.

## 3. Language Selection

Supported startup languages:

- RU — Русский
- EN — English
- FR — Français
- ES — Español
- UA — Українська

If the user's conversational language is obvious, it may be presented first as a suggested candidate. It is not confirmed until the user explicitly confirms it.

If the language is already explicitly confirmed in the current startup, do not ask again.

Language confirmation must happen before Mode confirmation.

### Mandatory Language → Mode Transition

When the user explicitly selects one supported language token or label (`RU`, `EN`, `FR`, `ES`, `UA`, or its displayed language name), that response MUST both:

1. record the Language as confirmed startup selection; and
2. immediately render the Mode Selection choices in the same assistant response.

An acknowledgement-only response such as "Continuing in Russian" is invalid. Do not stop after confirming Language. Do not perform an extra repository description, generic repository search, or unrelated fetch before showing Mode choices when the Startup Flow contract is already loaded and the supported Language selection is unambiguous.

Required transition:

`supported Language selected → Language confirmed → Mode choices shown immediately`

This transition still creates no project State and does not confirm any Mode.

## 4. Mode Selection

Available startup choices must be shown with one short, user-facing description for each option:

- **Standard** — structured project management with stages, tasks, plans, state, and completion control.
- **RPG** — real project presented as an adventure with chapters, quests, Boss Quests, map, progress, and achievements.
- **Sakura** — calm step-by-step project flow with a soft garden/path presentation.
- **Cyber** — technical control-center presentation with strict statuses, diagnostics, and system-style control.
- **Anime Magic** — expressive anime/magic presentation for a real project without RPG XP/level mechanics.
- **Executive** — decision-focused project mode for priorities, risks, metrics, and action plans.
- **Study** — learning mode with lessons, practice, review, knowledge checks, and learning progress.
- **Auto** — analyzes the stated goal and proposes one canonical Mode, but never activates it without confirmation.

The descriptions are explanatory UI text only. They do not alter canonical Mode identity, routing, locks, or project State.

### Mobile-first Mode Selection

The Mode selection surface must remain readable on a phone:

- show each Mode name first, followed by a concise description;
- prefer one compact bullet or short paragraph per Mode;
- avoid wide tables and horizontal scrolling;
- do not omit a Mode description merely to shorten the screen;
- keep all eight startup choices visible in the same Mode-selection response when practical;
- if the client visually wraps text, preserve the same Mode order and identity.

`Auto` is a startup selector, not a canonical runtime Mode and not an eighth Mode file family. It never appears in the 35 canonical Mode × Language × Version tuples.

Selecting `Auto` allows the AI to analyze the user's stated project goal and propose one canonical Mode. Show a short reason and require explicit user confirmation. Auto must never silently activate a Mode.

## 5. Mode Confirmation

After Language and Mode are selected, show at least:

- confirmed Language;
- selected Mode;
- a short Mode description;
- an explicit confirmation question.

Example:

`Язык: Русский`

`Стиль: RPG`

`Формат: реальный проект как RPG-приключение с главами, квестами, картой и достижениями.`

`Подтвердить этот стиль?`

The selected Mode remains only a requested Mode until explicitly confirmed.

## 6. Startup Lock

Until both Language and Mode are explicitly confirmed, do not:

- create or confirm a project;
- create a Project ID;
- create Progress or Current Position;
- create project State;
- open Stage 1;
- activate Task 1.1;
- activate Quest 1.1;
- activate Step 1.1;
- award XP or another progress metric;
- claim that Start Lock has passed.

Startup Lock is additive. It does not replace Start Lock, Project Lock, Task/Quest/Step Lock, or Final confirmation.

After Language and Mode confirmation, Startup Lock releases control to Main Router. The loaded Mode's own Start Lock remains active until its separate project-start confirmation is satisfied.

## 7. Start Trigger Aliases

The following new-project intents start Startup Flow when they refer to Universal Prompt System:

- `новый`
- `новый проект`
- `начало`
- `старт`
- `start`
- `new project`

Equivalent unambiguous localized phrases may normalize to the same intent.

These aliases start the sequence; they do not confirm Language, Mode, project scope, or Start.

## 8. Main Router Handoff

Only after Language and Mode are confirmed:

1. Requested Language = confirmed startup Language.
2. Requested Mode = confirmed canonical Mode.
3. Requested Prompt Version = `v1.0`.
4. Main Router resolves exactly one canonical row in `MODES.md`.
5. Main Router verifies file metadata and identity.
6. The selected Mode is loaded.
7. The selected Mode displays its normal Start Screen.
8. The selected Mode's Start Lock controls Project ID and active project State creation.

Startup Flow never bypasses Main Router validation.

## 9. Resume Behavior

Resume is not a new-project startup.

For a valid Project Export or explicit Resume, use the existing Resume routing contract and validate the pinned Mode, Language, Version, Project ID, Route, and State.

Do not force Language/Mode re-selection for a valid Resume. A conflict, damaged Export, or ambiguous identity opens Recovery.

If the user explicitly requests a new project instead of Resume, run Startup Flow and do not inherit old confirmed project State.

## 10. Error / Recovery Behavior

Open Recovery or Fallback when:

- the requested Language is unsupported;
- the selected Mode is not canonical;
- Auto cannot make a safe proposal from the available goal;
- confirmed startup values conflict with a valid Resume Export;
- Main Router cannot resolve exactly one canonical tuple;
- selected file metadata does not match the confirmed tuple.

Recovery shows confirmed, conflicting, and unknown data and does not create project State while unresolved.

## 11. Minimal Startup State

Before project creation, only minimal startup selections may be tracked:

- Startup status;
- Language candidate / confirmation;
- Mode candidate / confirmation;
- Auto proposal when applicable.

These values are not project State and must not be represented as Project ID, Current Position, Progress, Checkpoint, or completed work.

## 12. Cross-Language Parity

Functional order and locks are identical in RU, EN, FR, ES, and UA. Labels may be localized, but these invariants cannot change:

`Language → Mode → Confirmation → Router → Mode Start`

No language variant may silently select a Mode or create project State earlier than another.

## 13. Non-Negotiable Result

If repository entry only describes the repository, if Mode activates before confirmation, if Language is skipped without explicit confirmation, if Auto activates silently, or if Project ID / active work opens before the selected Mode's Start Lock, the startup implementation is `NOT READY`.
