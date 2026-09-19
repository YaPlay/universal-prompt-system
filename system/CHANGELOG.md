# CHANGELOG

## Universal Prompt System v1.0 — 2026-09-19

Initial public release of the Universal Prompt System prompt set (published 2026-09-19).

### Included

- seven isolated Modes: Standard, RPG, Sakura, Cyber, Anime Magic, Executive, and Study;
- five language variants for every Mode: RU, EN, FR, ES, and UA;
- deterministic Router and canonical registry for all 35 Mode × Language × Prompt Version tuples;
- Core locks for Mode Entry, language/version pinning, task scope, persistent interface, state isolation, recovery, and Reality First;
- explicit Project Export, Project Copy, Resume, Final confirmation, and history-preserving Reopen contracts;
- mobile-first command surfaces, localized documentation, structural QA, parity checks, and adversarial regression coverage.

This repository is a declarative prompt specification. It does not include an executable Router or runtime persistence service.

## Core System Hardening v1.0

Integrated the system-layer contracts for:

- Router-first Mode, Language, and Version resolution;
- System Layer Lock and Mode Entry Lock;
- Mode Heartbeat and Recovery on conflicts;
- Command Namespace Lock and foreign-command rejection;
- Mode/Language/Version pinning without silent upgrade or downgrade;
- Project Layer Isolation and Prompt / Artifact Isolation;
- Old Context Isolation and explicit State Source Priority;
- stable Project ID isolation;
- distinct Project Copy and Project Export semantics;
- Resume of the same pinned project without a new Start;
- Final confirmation and history-preserving Reopen;
- structural, semantic, regression, adversarial, cross-mode, and cross-language QA.

No mode-specific RPG, Sakura, Cyber, Anime Magic, Executive, Study, or Standard mechanics were replaced by the system layer.
