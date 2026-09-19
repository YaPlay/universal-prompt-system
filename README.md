# Universal Prompt System

Universal Prompt System is a prompt-based, declarative framework for running structured projects through a Router and a set of isolated interaction Modes. It defines state, routing, locks, recovery, planning, saving, export, resume, final confirmation, and reopen behavior in Markdown prompt files.

The repository contains seven Modes:

- Standard — neutral project workflow;
- RPG — quests and confirmed RPG progression;
- Sakura — paths, steps, and a digital garden;
- Cyber — control-center workflow;
- Anime Magic — atmospheric magic UI without RPG progression;
- Executive — decisions, risks, metrics, and action plans;
- Study — structured learning without invented mastery.

Each Mode is available in five languages: RU, EN, FR, ES, and UA. The current release is `v1.0`; Mode files are marked `Status: Final`.

## How to choose a Mode and Language

Request an exact tuple:

```text
Mode + Language + Prompt Version
```

For this release, use one of the registered combinations in [`system/MODES.md`](system/MODES.md) with `Prompt Version: v1.0`. The Router must load the exact canonical file and must not silently substitute another Mode, language, or version.

## System and Router

Read [`system/START-HERE.md`](system/START-HERE.md) first, then the Core System, Router, registry, and version map. The system layer loads before a Mode. It validates the tuple, applies Core Locks, and hands off to exactly one registered Mode file. Conflicts, missing files, damaged exports, and ambiguous state go to `Fallback` or `Recovery`.

## Repository structure

```text
README.md
LICENSE
docs/
system/
prompts/<mode>/<mode>-<language>-v1.0.md
assets/
```

- [`system/`](system/) — Core hardening, Router, registry, version map, QA checklist, and onboarding;
- [`prompts/`](prompts/) — 35 canonical Mode × Language prompt files;
- [`docs/`](docs/) — localized project documentation;
- [`assets/`](assets/) — reserved for project assets.

## Documentation

- [Русская документация](docs/README-RU.md)
- [English documentation](docs/README-EN.md)
- [Documentation française](docs/README-FR.md)
- [Documentación en español](docs/README-ES.md)
- [Українська документація](docs/README-UA.md)

## Status

The v1.0 prompt set and system layer are the initial public release. This repository is declarative: it contains Markdown prompt contracts and documentation, not an executable application or a standalone Router binary.

## Contributing

- [Read the contribution guide](CONTRIBUTING.md).
- [Report a bug](https://github.com/YaPlay/universal-prompt-system/issues/new?template=bug_report.yml).
- [Request a feature](https://github.com/YaPlay/universal-prompt-system/issues/new?template=feature_request.yml).

## Licensing

Project materials are released under [CC BY 4.0](LICENSE). Attribution is required for sharing or adapting the material. See the license for the complete terms.

## Disclaimer

Universal Prompt System is a prompt-based/declarative specification. It does not itself execute a Router, persist project state, validate external facts, or provide a production runtime. Any host application or model integration must implement the declared contracts and should perform its own safety and operational checks.
