# MODE REGISTRY — v1.0

Status: Final

This registry is the canonical identity and command namespace table used by the Main Router. The Main Router enforces the `Command Namespace Lock`; Mode UI cannot override Core Locks.

## Universal Core namespace

Every Mode inherits these commands:

`Главное меню` · `Задача/Шаг/Квест` · `План` · `Состояние` · `Задачи/Шаги/Квесты` · `Полный план` · `Сохранить` · `Настройки` · `Команды` · `Продолжить` · `Назад`

The localized label may vary, but the function and namespace identity do not. Contextual actions remain separate unless explicitly registered below.

## Canonical modes

| Mode | Canonical identity | Startup label | Short description | RU file | Mode-specific namespace | Isolation rule |
|---|---|---|---|---|---|---|
| Standard | `Standard` | Standard | Neutral structured project workflow | `prompts/standard/STANDARD-RU-v1.0.md` | `Ресурсы проекта`, `Контрольная точка`, `Копия проекта`, `Экспорт проекта`, `Восстановление` | Neutral workflow; no RPG, Sakura, Cyber, magic, executive, or study state |
| RPG | `RPG` | RPG | Real project as chapters, quests, maps, and confirmed progression | `prompts/rpg/RPG-QUEST-MODE-RU-v1.0.md` | `Профиль`, `Карта`, `Полная карта`, `Цели квеста`, `Компас`, `Журнал квестов`, `Лагерь восстановления`, `Инвентарь`, `Достижения`, `Босс-квест` | RPG UI and metrics require real confirmed project data |
| Sakura | `Sakura` | Sakura | Calm digital-garden workflow with paths and steps | `prompts/sakura/SAKURA-RU-v1.0.md` | `Шаг`, `Шаги`, `Состояние сада`, `Ресурсы сада`, `Садовая точка`, `Дополнительный шаг`, `Ключевой шаг`, `Восстановление` | Adult digital garden; no RPG stats or fake growth |
| Cyber | `Cyber` | Cyber | Technical control-center workflow | `prompts/cyber/CYBER-RU-v1.0.md` | `Состояние системы`, `Точка синхронизации`, `Системные ресурсы`, `Диагностика`, `Подключения`, `Восстановление` | Control-center UI; no fake signals, connections, or diagnostics |
| Anime Magic | `Anime Magic` | Anime Magic | Atmospheric anime-magic project interface without RPG progression | `prompts/anime-magic/ANIME-MAGIC-RU-v1.0.md` | `Магическое состояние`, `Артефакты`, `Точка сохранения`, `Выбор пути`, `Риски`, `Озарения`, `Режим тишины`, `Восстановление` | Atmospheric magic UI; no RPG progression or fake lore/state |
| Executive | `Executive` | Executive | Decision, risk, metric, owner, and deadline dashboard | `prompts/executive/EXECUTIVE-RU-v1.0.md` | `Решения`, `Риски`, `Метрики`, `Action Plan`, `Owners`, `Deadlines`, `Контрольная точка`, `Восстановление` | Dashboard semantics; no invented KPIs, owners, or deadlines |
| Study | `Study` | Study | Structured learning companion with lessons and knowledge checks | `prompts/study/STUDY-RU-v1.0.md` | `Тема`, `Урок`, `Проверка знаний`, `Карта знаний`, `Ошибки и пробелы`, `Повторение`, `Учебные материалы`, `Восстановление` | Adult learning companion; no invented understanding, mastery, mistakes, difficulty, or progress |

### Startup-only selector: Auto

`Auto` is supported by `STARTUP-FLOW-v1.0.md` as a selector only. It analyzes the user's stated goal and proposes exactly one canonical Mode with a short reason. It never activates a Mode without explicit confirmation and does not add an eighth Mode, canonical path family, or registry tuple.

## Canonical path registry

The Main Router must resolve the exact tuple `Mode + Language + Prompt Version` through this registry. The registry is exhaustive for the v1.0 release: every tuple has exactly one canonical path, and no path may serve more than one tuple.

| Mode | Language | Prompt Version | Canonical path |
|---|---|---|---|
| Standard | RU | v1.0 | `prompts/standard/STANDARD-RU-v1.0.md` |
| Standard | EN | v1.0 | `prompts/standard/STANDARD-EN-v1.0.md` |
| Standard | FR | v1.0 | `prompts/standard/STANDARD-FR-v1.0.md` |
| Standard | ES | v1.0 | `prompts/standard/STANDARD-ES-v1.0.md` |
| Standard | UA | v1.0 | `prompts/standard/STANDARD-UA-v1.0.md` |
| RPG | RU | v1.0 | `prompts/rpg/RPG-QUEST-MODE-RU-v1.0.md` |
| RPG | EN | v1.0 | `prompts/rpg/RPG-QUEST-MODE-EN-v1.0.md` |
| RPG | FR | v1.0 | `prompts/rpg/RPG-QUEST-MODE-FR-v1.0.md` |
| RPG | ES | v1.0 | `prompts/rpg/RPG-QUEST-MODE-ES-v1.0.md` |
| RPG | UA | v1.0 | `prompts/rpg/RPG-QUEST-MODE-UA-v1.0.md` |
| Sakura | RU | v1.0 | `prompts/sakura/SAKURA-RU-v1.0.md` |
| Sakura | EN | v1.0 | `prompts/sakura/SAKURA-EN-v1.0.md` |
| Sakura | FR | v1.0 | `prompts/sakura/SAKURA-FR-v1.0.md` |
| Sakura | ES | v1.0 | `prompts/sakura/SAKURA-ES-v1.0.md` |
| Sakura | UA | v1.0 | `prompts/sakura/SAKURA-UA-v1.0.md` |
| Cyber | RU | v1.0 | `prompts/cyber/CYBER-RU-v1.0.md` |
| Cyber | EN | v1.0 | `prompts/cyber/CYBER-EN-v1.0.md` |
| Cyber | FR | v1.0 | `prompts/cyber/CYBER-FR-v1.0.md` |
| Cyber | ES | v1.0 | `prompts/cyber/CYBER-ES-v1.0.md` |
| Cyber | UA | v1.0 | `prompts/cyber/CYBER-UA-v1.0.md` |
| Anime Magic | RU | v1.0 | `prompts/anime-magic/ANIME-MAGIC-RU-v1.0.md` |
| Anime Magic | EN | v1.0 | `prompts/anime-magic/ANIME-MAGIC-EN-v1.0.md` |
| Anime Magic | FR | v1.0 | `prompts/anime-magic/ANIME-MAGIC-FR-v1.0.md` |
| Anime Magic | ES | v1.0 | `prompts/anime-magic/ANIME-MAGIC-ES-v1.0.md` |
| Anime Magic | UA | v1.0 | `prompts/anime-magic/ANIME-MAGIC-UA-v1.0.md` |
| Executive | RU | v1.0 | `prompts/executive/EXECUTIVE-RU-v1.0.md` |
| Executive | EN | v1.0 | `prompts/executive/EXECUTIVE-EN-v1.0.md` |
| Executive | FR | v1.0 | `prompts/executive/EXECUTIVE-FR-v1.0.md` |
| Executive | ES | v1.0 | `prompts/executive/EXECUTIVE-ES-v1.0.md` |
| Executive | UA | v1.0 | `prompts/executive/EXECUTIVE-UA-v1.0.md` |
| Study | RU | v1.0 | `prompts/study/STUDY-RU-v1.0.md` |
| Study | EN | v1.0 | `prompts/study/STUDY-EN-v1.0.md` |
| Study | FR | v1.0 | `prompts/study/STUDY-FR-v1.0.md` |
| Study | ES | v1.0 | `prompts/study/STUDY-ES-v1.0.md` |
| Study | UA | v1.0 | `prompts/study/STUDY-UA-v1.0.md` |

Resolution is deterministic: exactly one matching registry row is required. Zero matches use `Fallback` or `Recovery`; duplicate matches are a registry error and require `Recovery`. The Router must not use directory order, file timestamps, glob order, or a user-facing label as a tie-breaker.

## Namespace enforcement

- The active Mode namespace is selected from the loaded canonical identity, not from a user-facing label alone.
- A command from another Mode is not executed, renamed silently, or treated as a universal command.
- Translation files inherit the same namespace functions and must not introduce a foreign Mode command.
- `Project Export` and `Project Copy` are universal mechanisms with distinct semantics in every namespace.
- Start Lock, Task/Quest Lock, Single State, Reality First, Final confirmation, and Reopen remain mandatory in every Mode.
