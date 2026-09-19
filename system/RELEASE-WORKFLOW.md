# Universal Prompt System — Version and Release Workflow

Status: Final

This document defines how repository releases and Prompt Versions evolve. It
does not change the v1.0 Core, Router, Mode contracts, or the semantics of any
published project.

## Scope and source of truth

The canonical identity of a prompt is the exact tuple:

```text
Mode + Language + Prompt Version
```

`system/MODES.md` remains the canonical Mode × Language × Prompt Version path
registry. `system/VERSION-MAP.md` records the supported release/version
mapping, and the Router must resolve the exact registered tuple. This workflow
document explains release operations; it is not a replacement registry.

## Version meanings

### Patch releases: `v1.0.x`

Patch releases are limited to changes with no semantic contract change:

- typo corrections;
- documentation corrections;
- localization corrections that preserve behavior;
- non-breaking QA or repository maintenance;
- release hygiene updates.

A patch release must not silently change a Mode rule, command identity, state
mutation, lock, recovery behavior, Export/Copy schema, Resume behavior, or
other Core or Mode contract.

### Minor releases: `v1.x`

Minor releases may add backward-compatible functionality:

- new optional commands or features;
- additive behavior that does not invalidate existing projects;
- a new Mode only when the canonical registry, Router handoff, documentation,
  translations, and QA are updated explicitly.

Existing v1.0 project semantics must not silently change. A v1.1 project or
Mode may add capabilities, but a pinned v1.0 project continues to use its v1.0
contracts.

### Major releases: `v2.0`

Major releases may introduce breaking contract changes, including new routing
or state semantics. They require explicit migration rules, compatibility
documentation, and a migration or transition plan for existing projects.

## Immutable version rule

Once a Mode is released under an exact tuple:

```text
Mode + Language + Prompt Version
```

that tuple is immutable. For example, a released
`STANDARD-RU-v1.0.md` must not later receive silent semantic changes. A
semantic correction requires a new versioned file and a new registered tuple.
Documentation, repository metadata, and non-semantic QA maintenance may be
published as a repository patch while the Prompt Version remains unchanged.

Published tags and their reviewed commits are also immutable in practice:
never move or delete a published release tag and never force-push release
history.

## Exact version pinning

The Router and every Mode handoff follow these rules:

- resolve only an exact registered `Mode + Language + Prompt Version` tuple;
- never select `latest` automatically;
- never perform a silent upgrade;
- never perform a silent downgrade;
- resume a project with its exact pinned Prompt Version;
- send a missing requested version to `Fallback` or `Recovery`;
- do not let a future `v1.1` alter a running or resumed `v1.0` project.

Directory order, file timestamps, glob order, and user-facing labels are never
version-selection mechanisms.

## Repository release versus Prompt Version

The repository release version and the Prompt Version are related but distinct:

- **Repository Release** identifies a published repository snapshot, release
  notes, and tag.
- **Prompt Version** identifies the immutable Mode contract selected by the
  Router and stored in a project’s pinned tuple.

A repository patch can therefore be released as `v1.0.1` while the prompt
contracts remain `Prompt Version: v1.0`. This is valid when the patch changes
only repository, documentation, localization, QA, or release metadata and
does not change prompt semantics.

If a Mode contract’s semantics change, its Prompt Version must change. The
repository release notes must make that relationship explicit.

## Compatibility matrix

| Repository Release | Prompt Version | Breaking? | New Mode files? |
|---|---|---:|---|
| `v1.0` | `v1.0` | No | No; the existing 35 files are the release set |
| `v1.0.1` | `v1.0` possible | No | No, when the patch is repository/docs/QA-only |
| `v1.1` | `v1.1` if semantics or features changed | No, when backward-compatible | Only if explicitly added and registered |
| `v2.0` | `v2.0` | Yes, where contracts break | As required by the migration plan |

The matrix is a compatibility guide, not permission to silently retag or
rewrite an existing tuple.

## New release workflow

Use this order for every future release:

1. Create a release branch from the reviewed base.
2. Copy or introduce new versioned files where a Prompt Version actually
   changes; do not duplicate files for a repository-only patch.
3. Update the canonical registry in `system/MODES.md`.
4. Update `system/VERSION-MAP.md`.
5. Update Router compatibility only explicitly and document any new tuple.
6. Update localized documentation and `system/CHANGELOG.md`.
7. Run the local QA script: `python scripts/qa.py`.
8. Run GitHub Actions for the branch and pull request.
9. Perform semantic and cross-language audits for every affected tuple.
10. Run adversarial regression, including Resume, Recovery, Export, Copy,
    Final, Reopen, locks, and no-silent-fallback behavior.
11. Review and commit the release changes, then push the branch.
12. Create an annotated tag on the exact reviewed commit.
13. Publish the GitHub Release with matching target commit and release notes.
14. Perform external verification of the tag, release, registry, files, and
    working tree.

No step may use `latest` as a substitute for an exact version, and no release
step may move an existing published tag.

## Patch rule: `v1.0.1` without 35 new prompt files

If `v1.0.1` changes only repository files, documentation, QA, or other release
hygiene and does **not** change a Prompt contract, creating 35 new
`v1.0.1` Mode files is neither required nor desirable:

```text
Repository Release: v1.0.1
Prompt Version:    v1.0
```

This keeps the existing exact tuple immutable while recording a newer
repository snapshot. If prompt semantics change, the affected Prompt Version
must be versioned and registered explicitly; do not hide that change in a
repository-only patch.

## QA compatibility and version allowlists

The current `scripts/qa.py` uses an explicit v1.0 release contract for the
current `main` branch: exact v1.0 metadata, 35 Mode files, 7 canonical Core
system files, registry parity, and the published section counts. The checks do
not search for a highest or latest file. The canonical registry remains the
authority for every tuple.

The QA architecture separates reusable checks from the current release
contract. A future release can update an explicit version allowlist or
manifest and its expected section contract on a reviewed branch; it must not
replace exact matching with automatic version selection. Auxiliary system
documents, such as this workflow, are allowed without changing the count of
the 7 canonical Core system files.

No separate release manifest is required while `system/MODES.md`,
`system/VERSION-MAP.md`, and the explicit QA release contract remain
sufficient. Add a dedicated manifest only when it provides a new source of
truth rather than duplicating those records.

## Release safety

Every release must satisfy all of the following:

- never move or delete a published tag;
- never force-push release history;
- point the release tag to the exact reviewed commit;
- keep old Mode versions available for pinned projects and Resume;
- preserve Project Export versus Project Copy semantics;
- record migration and every breaking change in the changelog;
- verify the published tag, release target, registry, and working tree after
  publication.

For a major release, the changelog must identify affected tuples, migration
steps, compatibility limits, and any required user confirmation. A patch or
minor release must state why existing pinned projects remain safe.

## Release completion gate

A release is complete only when local QA and GitHub Actions pass, the relevant
semantic and cross-language audits pass, internal links are valid, metadata and
section numbering are correct, no forbidden repository leakage is present,
and the tag/release target the exact reviewed commit. A failed check requires
Recovery through the release workflow; it must not be bypassed by weakening a
check or guessing missing state.
