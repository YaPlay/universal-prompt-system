# Universal Prompt System — Русский

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
