<div align="center">

**Language:** 🇷🇺 [RU](docs/README-RU.md) · 🇬🇧 **EN** · 🇫🇷 [FR](docs/README-FR.md) · 🇪🇸 [ES](docs/README-ES.md) · 🇺🇦 [UA](docs/README-UA.md)

</div>

<div align="center">

# Universal Prompt System

**A multilingual, mode-based prompt framework for running real projects with strict routing, state protection, recovery, and final validation.**

![Version](https://img.shields.io/badge/version-v1.0-blue)
![Modes](https://img.shields.io/badge/modes-7-purple)
![Languages](https://img.shields.io/badge/languages-5-green)
[![Repository QA](https://github.com/YaPlay/universal-prompt-system/actions/workflows/qa.yml/badge.svg)](https://github.com/YaPlay/universal-prompt-system/actions/workflows/qa.yml)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)

</div>

---

## What is Universal Prompt System?

Universal Prompt System is a declarative prompt framework for structured project work.

Instead of relying on one generic prompt, it separates:

- startup and onboarding;
- language selection;
- interaction style / Mode;
- routing;
- project state;
- locks and confirmations;
- recovery;
- saving and resume;
- final validation;
- reopening completed projects.

The repository is designed so an AI can recognize the system, route into one exact Mode and language, and keep project state isolated from prompt text, old context, examples, and unrelated Modes.

> **Reality First:** the system must never claim that real work, progress, files, fixes, tests, achievements, or completion happened without confirmation or objective evidence.

---

## Quick Start

Send the repository link to an AI:

```text
https://github.com/YaPlay/universal-prompt-system
```

The expected startup sequence is:

```text
Universal Prompt System detected.
↓
Choose Language
↓
Choose Style / Mode
↓
Confirm Mode
↓
Main Router
↓
Selected Mode
↓
Start Project
```

Supported languages:

`RU` · `EN` · `FR` · `ES` · `UA`

Available startup styles:

`Standard` · `RPG` · `Sakura` · `Cyber` · `Anime Magic` · `Executive` · `Study` · `Auto`

### Auto

`Auto` is **not an eighth runtime Mode**.

It analyzes the user's stated goal, proposes one canonical Mode, explains the choice briefly, and still requires explicit confirmation before activation.

---

## Startup Flow

New projects follow a strict pre-routing flow:

```text
Repository detected
        ↓
   Startup Flow
        ↓
     Language
        ↓
       Mode
        ↓
  Confirmation
        ↓
   Main Router
        ↓
  Selected Mode
        ↓
   Start Project
```

### Startup Lock

Before Language and Mode are explicitly confirmed, the system must not create:

- Project ID;
- Progress;
- Current Position;
- project State;
- Stage 1;
- Task 1.1;
- Quest 1.1;
- Step 1.1;
- XP or other progress metrics.

Startup Lock protects **pre-routing selection**.

After routing, the selected Mode's own **Start Lock** still protects actual project creation.

See [`system/STARTUP-FLOW-v1.0.md`](system/STARTUP-FLOW-v1.0.md).

---

## Modes

| Mode | Purpose |
|---|---|
| **Standard** | Neutral, structured project workflow |
| **RPG** | Real projects as chapters, quests, maps, bosses, and confirmed progression |
| **Sakura** | Calm digital-garden workflow with paths and steps |
| **Cyber** | Technical control-center style |
| **Anime Magic** | Atmospheric anime-magic interface without RPG progression |
| **Executive** | Decisions, risks, metrics, owners, deadlines, and action plans |
| **Study** | Structured learning with lessons, knowledge checks, and review |

Each Mode is isolated from the others and owns its own command namespace and presentation.

---

## Languages

Every canonical Mode is available in:

- 🇷🇺 Russian — `RU`
- 🇬🇧 English — `EN`
- 🇫🇷 French — `FR`
- 🇪🇸 Spanish — `ES`
- 🇺🇦 Ukrainian — `UA`

Current matrix:

**7 Modes × 5 Languages = 35 canonical Mode files**

The Router must resolve exactly one registered tuple:

```text
Mode + Language + Prompt Version
```

For the current release:

```text
Prompt Version: v1.0
```

No latest-file guessing, directory-order guessing, silent language substitution, silent Mode substitution, silent upgrade, or silent downgrade is allowed.

---

## Core Safety and State Rules

Universal Prompt System v1.0 includes system-level protections for:

- System Layer Lock;
- Mode Entry Lock;
- Mode Heartbeat;
- Mode Recovery;
- Command Namespace Lock;
- Task Scope Lock;
- Persistent Interface Lock;
- Project Layer Isolation;
- Prompt / Artifact Isolation;
- Old Context Isolation;
- State Source Priority;
- Version Pinning;
- Single State;
- Reality First;
- no silent upgrade;
- no silent downgrade.

Mode-specific UI can extend the experience, but it cannot disable Core Locks.

---

## Start, Save, Resume, Final

### Start

A new Project ID is created only after the selected Mode's explicit Start confirmation.

### Save / Export

A Project Export represents the same project and preserves its identity and pinned tuple.

### Project Copy

A Project Copy is a new project and receives a new Project ID after its own Start confirmation.

### Resume

A valid Resume restores the same:

- Project ID;
- Mode;
- Language;
- Version;
- Route;
- Current Position;
- statuses;
- history;
- settings;
- Checkpoints;
- Important Decisions;
- Mode-specific State.

### Final

Final completion requires validation **and a separate explicit confirmation**.

### Reopen

Reopen keeps the same Project ID and preserves the old Final in history.

---

## Repository Structure

```text
universal-prompt-system/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── system/
│   ├── START-HERE.md
│   ├── STARTUP-FLOW-v1.0.md
│   ├── CORE-SYSTEM-HARDENING-v1.0.md
│   ├── MAIN-ROUTER-v1.0.md
│   ├── MODES.md
│   ├── VERSION-MAP.md
│   ├── QA-CHECKLIST.md
│   ├── RELEASE-WORKFLOW.md
│   ├── MAINTENANCE.md
│   └── CHANGELOG.md
├── prompts/
│   ├── standard/
│   ├── rpg/
│   ├── sakura/
│   ├── cyber/
│   ├── anime-magic/
│   ├── executive/
│   └── study/
├── docs/
├── scripts/
│   └── qa.py
└── assets/
```

---

## System Entry Points

Start here:

1. [`system/START-HERE.md`](system/START-HERE.md)
2. [`system/STARTUP-FLOW-v1.0.md`](system/STARTUP-FLOW-v1.0.md)
3. [`system/CORE-SYSTEM-HARDENING-v1.0.md`](system/CORE-SYSTEM-HARDENING-v1.0.md)
4. [`system/MAIN-ROUTER-v1.0.md`](system/MAIN-ROUTER-v1.0.md)
5. [`system/MODES.md`](system/MODES.md)
6. [`system/VERSION-MAP.md`](system/VERSION-MAP.md)

---

## Localized Documentation

- 🇷🇺 [Русская документация](docs/README-RU.md)
- 🇬🇧 [English documentation](docs/README-EN.md)
- 🇫🇷 [Documentation française](docs/README-FR.md)
- 🇪🇸 [Documentación en español](docs/README-ES.md)
- 🇺🇦 [Українська документація](docs/README-UA.md)

---

## QA and Release Validation

The repository includes automated structural and release QA:

```bash
python scripts/qa.py
```

The GitHub Actions workflow runs:

**Structural and release QA**

Current QA covers:

- canonical file counts;
- 35 registered Mode × Language tuples;
- metadata and version consistency;
- continuous section numbering;
- Markdown code-fence integrity;
- internal links;
- repository leakage checks;
- public-release hygiene;
- Startup Flow contract;
- registry consistency.

A real QA failure means the release is **NOT READY** until fixed and rerun.

See [`system/QA-CHECKLIST.md`](system/QA-CHECKLIST.md).

---

## Version

Current public release:

**Universal Prompt System v1.0**

The v1.0 compatibility layer includes:

```text
Core System Hardening v1.0
+
Startup Flow v1.0
+
Mode
+
Language
+
Prompt Version v1.0
```

See [`system/VERSION-MAP.md`](system/VERSION-MAP.md) and [`system/CHANGELOG.md`](system/CHANGELOG.md).

---

## Contributing

Contributions are welcome when they preserve system isolation, parity, routing, and Core Locks.

- [Contribution Guide](CONTRIBUTING.md)
- [Report a Bug](https://github.com/YaPlay/universal-prompt-system/issues/new?template=bug_report.yml)
- [Request a Feature](https://github.com/YaPlay/universal-prompt-system/issues/new?template=feature_request.yml)

---

## Security

For security-related guidance, see [`SECURITY.md`](SECURITY.md).

Do not publish secrets, private keys, access tokens, personal file paths, or environment files in the repository.

---

## License

Universal Prompt System is released under **CC BY 4.0**.

You may share and adapt the material with attribution.

See [`LICENSE`](LICENSE) for the full terms.

---

## Important Note

Universal Prompt System is a **prompt-based declarative specification**.

It does not itself provide:

- a standalone Router binary;
- persistent storage;
- external fact validation;
- autonomous runtime execution.

Any host application or AI integration must implement the declared contracts faithfully and perform its own operational and safety checks.

---

<div align="center">

**Universal Prompt System v1.0**

Structured projects. Isolated Modes. Confirmed state. Reliable routing.

</div>
