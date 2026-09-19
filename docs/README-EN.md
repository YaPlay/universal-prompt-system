# Universal Prompt System — English

Universal Prompt System is a declarative Markdown prompt framework for structured project work. It separates a Core system layer from seven isolated Modes and routes an exact `Mode + Language + Prompt Version` tuple.

## Release

Current release: `v1.0`. The repository provides seven Modes in five languages: RU, EN, FR, ES, and UA.

Modes: Standard, RPG, Sakura, Cyber, Anime Magic, Executive, and Study.

Start with [`system/START-HERE.md`](../system/START-HERE.md), then read the Router and registry before loading a Mode. Only exact registered files may be selected; missing or conflicting data goes to `Fallback` or `Recovery`.

The system is prompt-based and declarative. It is not an executable Router or a persistence service.

See the [root README](../README.md) for the repository map and localized documentation.

