# Universal Prompt System — Русский

Universal Prompt System — декларативная Markdown-система промптов для структурированной работы над проектами. Core-слой отделён от семи изолированных режимов и использует точный tuple `Mode + Language + Prompt Version`.

## Релиз

Текущий релиз: `v1.0`. Доступны семь режимов на пяти языках: RU, EN, FR, ES и UA.

Режимы: Standard, RPG, Sakura, Cyber, Anime Magic, Executive и Study.

Начните с [`system/START-HERE.md`](../system/START-HERE.md), затем прочитайте Router и Registry перед загрузкой режима. Выбираются только точные зарегистрированные файлы; отсутствующие или конфликтующие данные направляются в `Fallback` или `Recovery`.

Система является prompt-based/declarative спецификацией. Это не исполняемый Router и не сервис хранения состояния.

См. [корневой README](../README.md) для карты репозитория и списка локализованных документов.

