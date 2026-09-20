<div align="center">

**Язык:** 🇷🇺 **RU** · 🇬🇧 [EN](../README.md) · 🇫🇷 [FR](README-FR.md) · 🇪🇸 [ES](README-ES.md) · 🇺🇦 [UA](README-UA.md)

</div>

# Universal Prompt System — Русский

![Version](https://img.shields.io/badge/version-v1.0-blue)
![Modes](https://img.shields.io/badge/modes-7-purple)
![Languages](https://img.shields.io/badge/languages-5-green)
[![Repository QA](https://github.com/YaPlay/universal-prompt-system/actions/workflows/qa.yml/badge.svg)](https://github.com/YaPlay/universal-prompt-system/actions/workflows/qa.yml)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)

**Многоязычная система промптов с режимами, строгой маршрутизацией, защитой состояния, Recovery и финальной проверкой.**

---

## Что такое Universal Prompt System?

Universal Prompt System — декларативный framework для структурированной работы над реальными проектами.

Система разделяет:

- запуск и onboarding;
- выбор языка;
- выбор Style / Mode;
- маршрутизацию;
- состояние проекта;
- Locks и подтверждения;
- Recovery;
- Save / Export / Resume;
- Final Validation;
- Reopen.

> **Reality First:** нельзя утверждать, что реальная работа, файл, исправление, тест, прогресс или завершение произошли без подтверждения пользователя или объективных данных.

---

## Быстрый старт

Отправьте ИИ ссылку:

```text
https://github.com/YaPlay/universal-prompt-system
```

Ожидаемый запуск:

```text
Universal Prompt System обнаружен
↓
Выбор языка
↓
Выбор Style / Mode
↓
Подтверждение Mode
↓
Main Router
↓
Выбранный Mode
↓
Старт проекта
```

Языки:

`RU` · `EN` · `FR` · `ES` · `UA`

Стили:

`Standard` · `RPG` · `Sakura` · `Cyber` · `Anime Magic` · `Executive` · `Study` · `Auto`

### Auto

`Auto` — это не восьмой runtime Mode.

Он анализирует цель пользователя, предлагает один канонический Mode и всё равно требует явного подтверждения перед активацией.

---

## Startup Flow

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

До подтверждения Language и Mode система не должна создавать:

- Project ID;
- Progress;
- Current Position;
- project State;
- Stage 1;
- Task 1.1;
- Quest 1.1;
- Step 1.1;
- XP или другие метрики прогресса.

После Startup Lock выбранный Mode всё ещё применяет собственный Start Lock.

См. [STARTUP-FLOW-v1.0.md](../system/STARTUP-FLOW-v1.0.md).

---

## Режимы

| Mode | Назначение |
|---|---|
| **Standard** | Нейтральная структурированная работа над проектом |
| **RPG** | Главы, квесты, карты, Boss Quests и подтверждённый прогресс |
| **Sakura** | Спокойный digital garden с путями и шагами |
| **Cyber** | Технический control-center стиль |
| **Anime Magic** | Атмосферный магический интерфейс без RPG-прогрессии |
| **Executive** | Решения, риски, метрики, owners, deadlines и action plans |
| **Study** | Структурированное обучение, уроки и проверка знаний |

---

## Языки и canonical matrix

Каждый Mode доступен на пяти языках:

- 🇷🇺 RU
- 🇬🇧 EN
- 🇫🇷 FR
- 🇪🇸 ES
- 🇺🇦 UA

**7 Modes × 5 Languages = 35 canonical Mode files**

Router разрешает только точный tuple:

```text
Mode + Language + Prompt Version
```

Текущая версия: `v1.0`.

Запрещены silent Mode switch, silent language switch, silent upgrade и silent downgrade.

---

## Core правила

Система включает:

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
- Reality First.

Mode UI может расширять интерфейс, но не может отключать Core Locks.

---

## Start / Save / Resume / Final

- **Start:** новый Project ID создаётся только после явного подтверждения старта выбранного Mode.
- **Project Export:** сохраняет тот же проект и тот же Project ID.
- **Project Copy:** создаёт новый проект.
- **Resume:** восстанавливает тот же Project ID, Mode, Language, Version, Route, Current Position и историю.
- **Final:** требует проверки и отдельного явного подтверждения.
- **Reopen:** сохраняет старый Final в истории и продолжает тот же Project ID.

---

## QA

Локальная проверка:

```bash
python scripts/qa.py
```

GitHub Actions запускает:

**Structural and release QA**

Проверяются canonical files, 35 tuples, metadata, numbering, Markdown, internal links, repository hygiene, Startup Flow и registry consistency.

Любой реальный FAIL означает: **NOT READY**.

См. [QA-CHECKLIST.md](../system/QA-CHECKLIST.md).

---

## Версия

**Universal Prompt System v1.0**

Совместимость:

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

См. [VERSION-MAP.md](../system/VERSION-MAP.md) и [CHANGELOG.md](../system/CHANGELOG.md).

---

## Полезные ссылки

- [Главный README](../README.md)
- [START HERE](../system/START-HERE.md)
- [Startup Flow](../system/STARTUP-FLOW-v1.0.md)
- [Main Router](../system/MAIN-ROUTER-v1.0.md)
- [Mode Registry](../system/MODES.md)
- [Contributing](../CONTRIBUTING.md)
- [Security](../SECURITY.md)
- [License](../LICENSE)

Universal Prompt System — prompt-based декларативная спецификация, а не самостоятельное приложение или runtime.

---

## Структура репозитория

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

## Системные точки входа

1. [START-HERE](../system/START-HERE.md)
2. [STARTUP-FLOW-v1.0](../system/STARTUP-FLOW-v1.0.md)
3. [CORE-SYSTEM-HARDENING-v1.0](../system/CORE-SYSTEM-HARDENING-v1.0.md)
4. [MAIN-ROUTER-v1.0](../system/MAIN-ROUTER-v1.0.md)
5. [MODES](../system/MODES.md)
6. [VERSION-MAP](../system/VERSION-MAP.md)

## Полное поведение проекта

### Start

Новый Project ID создаётся только после явного подтверждения старта выбранного Mode.

### Save / Export

Project Export относится к тому же проекту и сохраняет его identity и pinned tuple.

### Project Copy

Project Copy создаёт новый проект и получает новый Project ID только после собственного подтверждения старта.

### Resume

Корректный Resume восстанавливает тот же Project ID, Mode, Language, Version, Route, Current Position, statuses, history, settings, Checkpoints, Important Decisions и Mode-specific State.

### Final

Финальное завершение требует проверки и отдельного явного подтверждения.

### Reopen

Reopen сохраняет тот же Project ID и оставляет предыдущий Final в истории.

## Contributing

Вклад приветствуется, если он сохраняет system isolation, translation parity, routing и Core Locks.

- [Contribution Guide](../CONTRIBUTING.md)
- [Сообщить об ошибке](https://github.com/YaPlay/universal-prompt-system/issues/new?template=bug_report.yml)
- [Предложить функцию](https://github.com/YaPlay/universal-prompt-system/issues/new?template=feature_request.yml)

## Безопасность

См. [SECURITY.md](../SECURITY.md). Не публикуйте secrets, private keys, access tokens, личные file paths или environment files.

## Лицензия

Universal Prompt System распространяется по лицензии **CC BY 4.0**. Материалы можно распространять и адаптировать с указанием авторства. Полные условия: [LICENSE](../LICENSE).

## Важное примечание

Universal Prompt System — **prompt-based декларативная спецификация**. Она сама по себе не предоставляет отдельный Router binary, persistent storage, external fact validation или autonomous runtime execution. Любая host application или AI integration должна реализовать заявленные contracts и выполнять собственные operational и safety checks.
