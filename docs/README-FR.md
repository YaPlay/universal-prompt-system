# Universal Prompt System — Français

**Un système de prompts multilingue, basé sur des Modes, avec routage strict, protection de l'état, Recovery et validation finale.**

---

## Qu'est-ce que Universal Prompt System ?

Universal Prompt System est un framework déclaratif pour gérer des projets réels de manière structurée.

Il sépare le démarrage, la langue, le Mode, le routage, l'état du projet, les Locks, Recovery, Save / Export / Resume, Final Validation et Reopen.

> **Reality First :** aucune tâche, modification, progression, correction, validation ou création de fichier ne doit être présentée comme réelle sans confirmation ou preuve objective.

---

## Démarrage rapide

Envoyez au modèle :

```text
https://github.com/YaPlay/universal-prompt-system
```

Flux attendu :

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

Langues :

`RU` · `EN` · `FR` · `ES` · `UA`

Styles :

`Standard` · `RPG` · `Sakura` · `Cyber` · `Anime Magic` · `Executive` · `Study` · `Auto`

### Auto

`Auto` n'est pas un huitième Mode d'exécution.

Il analyse l'objectif déclaré, propose un Mode canonique et exige toujours une confirmation explicite avant activation.

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

Avant confirmation de Language et Mode, le système ne doit pas créer Project ID, Progress, Current Position, project State, Stage 1, Task 1.1, Quest 1.1, Step 1.1 ni XP.

Après le Startup Lock, le Start Lock propre au Mode choisi reste actif.

Voir [STARTUP-FLOW-v1.0.md](../system/STARTUP-FLOW-v1.0.md).

---

## Modes

| Mode | Objectif |
|---|---|
| **Standard** | Workflow de projet neutre et structuré |
| **RPG** | Chapitres, quêtes, cartes, Boss Quests et progression confirmée |
| **Sakura** | Digital garden calme avec chemins et étapes |
| **Cyber** | Interface de centre de contrôle technique |
| **Anime Magic** | Interface magique atmosphérique sans progression RPG |
| **Executive** | Décisions, risques, métriques, owners, deadlines et action plans |
| **Study** | Apprentissage structuré, leçons et vérifications de connaissances |

---

## Langues et matrice canonique

Chaque Mode existe en RU, EN, FR, ES et UA.

**7 Modes × 5 Languages = 35 canonical Mode files**

Le Router résout uniquement :

```text
Mode + Language + Prompt Version
```

Version actuelle : `v1.0`.

Aucun changement silencieux de Mode ou de langue, aucune mise à niveau ou rétrogradation silencieuse.

---

## Règles Core

Le système protège notamment Mode Entry, namespace des commandes, scope de tâche, interface persistante, isolation du projet, isolation Prompt / Artifact, ancien contexte, priorité des sources, version, Single State et Reality First.

Un Mode peut enrichir l'interface mais ne peut pas désactiver les Core Locks.

---

## Start / Save / Resume / Final

- **Start :** Project ID uniquement après confirmation explicite.
- **Project Export :** même projet, même Project ID.
- **Project Copy :** nouveau projet.
- **Resume :** restaure le même projet et son tuple épinglé.
- **Final :** validation + confirmation explicite séparée.
- **Reopen :** conserve l'ancien Final dans l'historique.

---

## QA

```bash
python scripts/qa.py
```

GitHub Actions exécute **Structural and release QA**.

Les contrôles couvrent les fichiers canoniques, 35 tuples, metadata, numérotation, Markdown, liens internes, hygiène du dépôt, Startup Flow et registre.

Tout vrai FAIL signifie **NOT READY**.

Voir [QA-CHECKLIST.md](../system/QA-CHECKLIST.md).

---

## Version

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

Voir [VERSION-MAP.md](../system/VERSION-MAP.md) et [CHANGELOG.md](../system/CHANGELOG.md).

---

## Liens utiles

- [README principal](../README.md)
- [START HERE](../system/START-HERE.md)
- [Startup Flow](../system/STARTUP-FLOW-v1.0.md)
- [Main Router](../system/MAIN-ROUTER-v1.0.md)
- [Mode Registry](../system/MODES.md)
- [Contributing](../CONTRIBUTING.md)
- [Security](../SECURITY.md)
- [License](../LICENSE)

Universal Prompt System est une spécification déclarative basée sur des prompts, pas une application runtime autonome.
