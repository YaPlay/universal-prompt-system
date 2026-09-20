# Universal Prompt System — Українська

**Багатомовна система промптів із режимами, суворою маршрутизацією, захистом стану, Recovery та фінальною перевіркою.**

---

## Що таке Universal Prompt System?

Universal Prompt System — декларативний framework для структурованої роботи над реальними проєктами.

Система розділяє запуск, мову, Mode, маршрутизацію, стан проєкту, Locks, Recovery, Save / Export / Resume, Final Validation і Reopen.

> **Reality First:** не можна стверджувати, що реальна робота, файл, виправлення, тест, прогрес або завершення відбулися без підтвердження чи об'єктивних даних.

---

## Швидкий старт

Надішліть моделі:

```text
https://github.com/YaPlay/universal-prompt-system
```

Очікуваний потік:

```text
Universal Prompt System detected
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

Мови:

`RU` · `EN` · `FR` · `ES` · `UA`

Стилі:

`Standard` · `RPG` · `Sakura` · `Cyber` · `Anime Magic` · `Executive` · `Study` · `Auto`

### Auto

`Auto` — не восьмий runtime Mode.

Він аналізує заявлену мету, пропонує один канонічний Mode і все одно вимагає явного підтвердження перед активацією.

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

До підтвердження Language і Mode система не повинна створювати Project ID, Progress, Current Position, project State, Stage 1, Task 1.1, Quest 1.1, Step 1.1 або XP.

Після Startup Lock власний Start Lock вибраного Mode залишається активним.

Див. [STARTUP-FLOW-v1.0.md](../system/STARTUP-FLOW-v1.0.md).

---

## Режими

| Mode | Призначення |
|---|---|
| **Standard** | Нейтральний структурований workflow проєкту |
| **RPG** | Глави, квести, карти, Boss Quests і підтверджений прогрес |
| **Sakura** | Спокійний digital garden зі шляхами та кроками |
| **Cyber** | Технічний control-center стиль |
| **Anime Magic** | Атмосферний магічний інтерфейс без RPG-прогресії |
| **Executive** | Рішення, ризики, метрики, owners, deadlines і action plans |
| **Study** | Структуроване навчання, уроки та перевірка знань |

---

## Мови та канонічна матриця

Кожен Mode доступний мовами RU, EN, FR, ES та UA.

**7 Modes × 5 Languages = 35 canonical Mode files**

Router розв'язує лише точний tuple:

```text
Mode + Language + Prompt Version
```

Поточна версія: `v1.0`.

Заборонені silent Mode switch, silent language switch, silent upgrade та silent downgrade.

---

## Core правила

Система захищає Mode Entry, command namespace, task scope, persistent interface, project isolation, Prompt / Artifact isolation, old context, source priority, version pinning, Single State та Reality First.

Mode може розширювати інтерфейс, але не може вимикати Core Locks.

---

## Start / Save / Resume / Final

- **Start:** Project ID створюється лише після явного підтвердження.
- **Project Export:** той самий проєкт і той самий Project ID.
- **Project Copy:** новий проєкт.
- **Resume:** відновлює той самий проєкт і закріплений tuple.
- **Final:** перевірка + окреме явне підтвердження.
- **Reopen:** зберігає попередній Final в історії.

---

## QA

```bash
python scripts/qa.py
```

GitHub Actions запускає **Structural and release QA**.

Перевіряються canonical files, 35 tuples, metadata, numbering, Markdown, internal links, repository hygiene, Startup Flow та registry consistency.

Будь-який реальний FAIL означає **NOT READY**.

Див. [QA-CHECKLIST.md](../system/QA-CHECKLIST.md).

---

## Версія

**Universal Prompt System v1.0**

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

Див. [VERSION-MAP.md](../system/VERSION-MAP.md) і [CHANGELOG.md](../system/CHANGELOG.md).

---

## Корисні посилання

- [Головний README](../README.md)
- [START HERE](../system/START-HERE.md)
- [Startup Flow](../system/STARTUP-FLOW-v1.0.md)
- [Main Router](../system/MAIN-ROUTER-v1.0.md)
- [Mode Registry](../system/MODES.md)
- [Contributing](../CONTRIBUTING.md)
- [Security](../SECURITY.md)
- [License](../LICENSE)

Universal Prompt System — декларативна prompt-based специфікація, а не автономний runtime-застосунок.
