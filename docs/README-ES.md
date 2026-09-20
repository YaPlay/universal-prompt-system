<div align="center">

**Idioma:** 🇷🇺 [RU](README-RU.md) · 🇬🇧 [EN](../README.md) · 🇫🇷 [FR](README-FR.md) · 🇪🇸 **ES** · 🇺🇦 [UA](README-UA.md)

</div>

# Universal Prompt System — Español

![Version](https://img.shields.io/badge/version-v1.0-blue)
![Modes](https://img.shields.io/badge/modes-7-purple)
![Languages](https://img.shields.io/badge/languages-5-green)
[![Repository QA](https://github.com/YaPlay/universal-prompt-system/actions/workflows/qa.yml/badge.svg)](https://github.com/YaPlay/universal-prompt-system/actions/workflows/qa.yml)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)

**Un sistema de prompts multilingüe basado en Modos, con enrutamiento estricto, protección del estado, Recovery y validación final.**

---

## ¿Qué es Universal Prompt System?

Universal Prompt System es un framework declarativo para trabajar con proyectos reales de forma estructurada.

Separa el inicio, el idioma, el Mode, el enrutamiento, el estado del proyecto, Locks, Recovery, Save / Export / Resume, Final Validation y Reopen.

> **Reality First:** ninguna tarea, archivo, corrección, progreso, prueba o finalización debe presentarse como real sin confirmación o evidencia objetiva.

---

## Inicio rápido

Envía al modelo:

```text
https://github.com/YaPlay/universal-prompt-system
```

Flujo esperado:

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

Idiomas:

`RU` · `EN` · `FR` · `ES` · `UA`

Estilos:

`Standard` · `RPG` · `Sakura` · `Cyber` · `Anime Magic` · `Executive` · `Study` · `Auto`

### Auto

`Auto` no es un octavo Mode de ejecución.

Analiza el objetivo declarado, propone un Mode canónico y sigue requiriendo confirmación explícita antes de activarlo.

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

Antes de confirmar Language y Mode, el sistema no debe crear Project ID, Progress, Current Position, project State, Stage 1, Task 1.1, Quest 1.1, Step 1.1 ni XP.

Después del Startup Lock, el Start Lock propio del Mode seleccionado sigue activo.

Consulta [STARTUP-FLOW-v1.0.md](../system/STARTUP-FLOW-v1.0.md).

---

## Modos

| Mode | Objetivo |
|---|---|
| **Standard** | Flujo neutral y estructurado para proyectos |
| **RPG** | Capítulos, quests, mapas, Boss Quests y progreso confirmado |
| **Sakura** | Digital garden tranquilo con rutas y pasos |
| **Cyber** | Interfaz técnica de centro de control |
| **Anime Magic** | Interfaz mágica atmosférica sin progresión RPG |
| **Executive** | Decisiones, riesgos, métricas, owners, deadlines y action plans |
| **Study** | Aprendizaje estructurado, lecciones y comprobaciones |

---

## Idiomas y matriz canónica

Cada Mode está disponible en RU, EN, FR, ES y UA.

**7 Modes × 5 Languages = 35 canonical Mode files**

El Router resuelve solo:

```text
Mode + Language + Prompt Version
```

Versión actual: `v1.0`.

No se permiten cambios silenciosos de Mode o idioma, ni silent upgrade ni silent downgrade.

---

## Reglas Core

El sistema protege Mode Entry, command namespace, task scope, persistent interface, project isolation, Prompt / Artifact isolation, old context, source priority, version pinning, Single State y Reality First.

Un Mode puede ampliar la experiencia, pero no puede desactivar los Core Locks.

---

## Start / Save / Resume / Final

- **Start:** Project ID solo después de confirmación explícita.
- **Project Export:** mismo proyecto y mismo Project ID.
- **Project Copy:** proyecto nuevo.
- **Resume:** restaura el mismo proyecto y su tuple fijado.
- **Final:** validación + confirmación explícita separada.
- **Reopen:** conserva el Final anterior en el historial.

---

## QA

```bash
python scripts/qa.py
```

GitHub Actions ejecuta **Structural and release QA**.

Se comprueban archivos canónicos, 35 tuples, metadata, numeración, Markdown, enlaces internos, higiene del repositorio, Startup Flow y registry consistency.

Cualquier FAIL real significa **NOT READY**.

Consulta [QA-CHECKLIST.md](../system/QA-CHECKLIST.md).

---

## Versión

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

Consulta [VERSION-MAP.md](../system/VERSION-MAP.md) y [CHANGELOG.md](../system/CHANGELOG.md).

---

## Enlaces útiles

- [README principal](../README.md)
- [START HERE](../system/START-HERE.md)
- [Startup Flow](../system/STARTUP-FLOW-v1.0.md)
- [Main Router](../system/MAIN-ROUTER-v1.0.md)
- [Mode Registry](../system/MODES.md)
- [Contributing](../CONTRIBUTING.md)
- [Security](../SECURITY.md)
- [License](../LICENSE)

Universal Prompt System es una especificación declarativa basada en prompts, no una aplicación runtime independiente.

---

## Estructura del repositorio

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

## Puntos de entrada del sistema

1. [START-HERE](../system/START-HERE.md)
2. [STARTUP-FLOW-v1.0](../system/STARTUP-FLOW-v1.0.md)
3. [CORE-SYSTEM-HARDENING-v1.0](../system/CORE-SYSTEM-HARDENING-v1.0.md)
4. [MAIN-ROUTER-v1.0](../system/MAIN-ROUTER-v1.0.md)
5. [MODES](../system/MODES.md)
6. [VERSION-MAP](../system/VERSION-MAP.md)

## Comportamiento completo del proyecto

### Start

Un nuevo Project ID se crea solo después de la confirmación explícita de inicio del Mode seleccionado.

### Save / Export

Project Export representa el mismo proyecto y conserva su identity y pinned tuple.

### Project Copy

Project Copy crea un proyecto nuevo y obtiene un nuevo Project ID solo después de su propia confirmación de inicio.

### Resume

Un Resume válido restaura el mismo Project ID, Mode, Language, Version, Route, Current Position, statuses, history, settings, Checkpoints, Important Decisions y Mode-specific State.

### Final

La finalización requiere validación y una confirmación explícita separada.

### Reopen

Reopen conserva el mismo Project ID y mantiene el Final anterior en el historial.

## Contribuciones

Las contribuciones son bienvenidas si preservan system isolation, translation parity, routing y Core Locks.

- [Contribution Guide](../CONTRIBUTING.md)
- [Informar de un error](https://github.com/YaPlay/universal-prompt-system/issues/new?template=bug_report.yml)
- [Solicitar una función](https://github.com/YaPlay/universal-prompt-system/issues/new?template=feature_request.yml)

## Seguridad

Consulta [SECURITY.md](../SECURITY.md). No publiques secrets, private keys, access tokens, rutas personales de archivos ni environment files.

## Licencia

Universal Prompt System se publica bajo **CC BY 4.0**. Puedes compartir y adaptar el material con atribución. Términos completos: [LICENSE](../LICENSE).

## Nota importante

Universal Prompt System es una **especificación declarativa basada en prompts**. No proporciona por sí mismo un Router binary independiente, persistent storage, external fact validation ni autonomous runtime execution. Cualquier host application o integración de IA debe implementar los contracts declarados y realizar sus propias comprobaciones operativas y de seguridad.
