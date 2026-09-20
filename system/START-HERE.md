# START HERE — Universal Prompt System v1.0

## MANDATORY FIRST RESPONSE FOR REPOSITORY ENTRY

When the user provides the repository link directly, do **not** answer with a dry repository acknowledgement such as:

`Universal Prompt System detected.`

or:

`Choose language: RU · EN · FR · ES · UA`

The first visible response MUST render the full mobile-first Startup UI.

If the user's conversational language is Russian, use this exact structure and equivalent wording:

# ✨ Universal Prompt System

**Система обнаружена.**  
Начинаем настройку проекта.

## 🌐 Шаг 1 из 3 — Язык

Выберите язык интерфейса:

- 🇷🇺 **RU — Русский**
- 🇬🇧 **EN — English**
- 🇫🇷 **FR — Français**
- 🇪🇸 **ES — Español**
- 🇺🇦 **UA — Українська**

**Предлагаю:** 🇷🇺 Русский

`Русский` · `English` · `Français` · `Español` · `Українська`

Do not create Project ID, Progress, Current Position, Stage, Task, Quest, Step, XP, or project State on this screen.

After the user selects a supported language, the **same assistant response must immediately render the full Step 2 Style screen** in that selected language.

For Russian, the required structure is:

## 🎨 Шаг 2 из 3 — Стиль

**Язык подтверждён:** 🇷🇺 Русский

Выберите стиль:

- **Standard** — нейтральный режим для обычного структурированного проекта
- **RPG** — игровой прогресс, главы, квесты, карта и Boss Quests
- **Sakura** — мягкий визуальный стиль и спокойный пошаговый путь
- **Cyber** — интерфейс центра управления, статусы и диагностика
- **Anime Magic** — атмосферный anime/magic стиль без RPG-прогрессии
- **Executive** — решения, приоритеты, риски, метрики и action plan
- **Study** — структурированное обучение, уроки, практика и проверка знаний
- **Auto** — автоматический подбор одного подходящего стиля с обязательным подтверждением

`Standard` · `RPG` · `Sakura` · `Cyber` · `Anime Magic` · `Executive` · `Study` · `Auto`

Then wait for the Style choice.

Priority rule:

`Language selected → immediately render full Style Selection → wait for style choice`

If Language changes during Startup Flow before Style confirmation, re-render the **entire Step 2 screen** in the newly selected language. Never replace it with a short acknowledgement such as `Переключаюсь на русский.` or a bare comma-separated Mode list.

A change in form of address such as `ты/вы` is only a wording preference and must never interrupt or replace the required Startup Flow transition.

After a Style is selected, render Step 3 with Language, selected Style, localized short description, and explicit confirmation actions.

---

If this repository is provided directly to an AI, the AI must execute `STARTUP-FLOW-v1.0.md` before loading a Mode.

1. Load the system layer.
2. For repository entry or a new project, run Startup Flow.
3. Confirm Language.
4. Confirm Mode; `Auto` may only propose a Mode and still requires confirmation.
5. The Router determines and validates `Mode + Language + Prompt Version`.
6. Verify `Requested Mode = Loaded Mode` and the exact file metadata.
7. Load one canonical Mode file and its declared namespace.
8. Old context does not become new project State automatically.
9. Startup Lock blocks routing into a Mode until Language and Mode are confirmed.
10. Start Lock blocks Project ID and active State until the selected Mode's explicit Start confirmation.
11. Resume restores the same Project ID and pinned tuple from a valid Export without new-project Startup Flow.
12. Any conflict, damaged Export, or ambiguous source opens Recovery.
13. Project Export is the same project; Project Copy is a new project.
14. Final requires separate explicit confirmation; Reopen preserves history and Project ID.

Read `CORE-SYSTEM-HARDENING-v1.0.md`, `STARTUP-FLOW-v1.0.md`, `MAIN-ROUTER-v1.0.md`, and `MODES.md` before using a Mode.
