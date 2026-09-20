# START HERE — Universal Prompt System v1.0

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
