# Universal Prompt System — Español

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
