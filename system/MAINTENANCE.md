# Universal Prompt System — Maintenance Contract

Status: Final

This contract governs post-release maintenance of the Universal Prompt System.
It preserves the published v1.0 Prompt contracts, exact version pinning, Core
locks, Router behavior, and the distinction between repository releases and
Prompt Versions.

## Published tuple and source of truth

The immutable identity of a released prompt is:

```text
Mode + Language + Prompt Version
```

`system/MODES.md` is the canonical tuple/path registry. `system/VERSION-MAP.md`
and `system/RELEASE-WORKFLOW.md` define version relationships and release
operations. A published tuple must not be edited in place to change semantics.

## Change classification matrix

Every issue must be classified before implementation. When a row says
"conditional," the decision and evidence must be written in the issue or pull
request.

| Change type | New Prompt Version? | New repository release? | Full regression? | Cross-language parity? | Adversarial regression? |
|---|---|---|---|---|---|
| Documentation-only | No | Optional patch release when published | Targeted local QA and link check; full regression not normally required | No, unless localized contract wording is touched | No, unless behavior could be affected |
| Localization-only | No when behavior and command identity are unchanged | Optional patch release when published | Targeted QA for all affected tuples | Yes for every affected language; expand to all five when contract wording is involved | Targeted when wording could alter behavior |
| QA/tooling | No | Optional patch release when published | Local QA and GitHub Actions are required; full prompt regression is not normally required | No, unless checks or translations change | No, unless the tooling changes runtime contract assumptions |
| Non-breaking prompt fix | No only when proven non-semantic; otherwise Yes for a released tuple | Patch release if repository-only; new Prompt Version if the tuple content changes | Yes, at least the affected Mode and all required parity checks | Yes when a contract or user-facing command is touched | Targeted or full, based on affected locks/state |
| Semantic prompt change | Yes | Yes | Yes | Yes, all five languages for the affected Mode | Yes |
| Breaking change | Yes | Yes, normally a major release | Yes | Yes, all five languages and migration checks | Yes |

"Full regression" includes the repository QA, Mode matrix, registry,
metadata, section numbering, code fences, links, and the relevant semantic
audits. A narrower check is allowed only when this table says it is targeted
and the reason is recorded.

## Bugfix flow

Use this order for every maintenance issue:

```text
Issue → reproduce → classify → fix → local QA → GitHub Actions → semantic/parity audit if needed → adversarial regression if needed → commit → PR/review → merge → release if required
```

The issue must identify the affected Mode, Language, Prompt Version, project
state or command namespace, and the evidence used for classification. A fix is
not complete because the text looks plausible; the real files and the stated
invariants must be checked.

## No-direct-semantic-edit rule

Semantic changes to a released Mode file cannot be made directly without a
version decision. The published tuple is immutable. If a change affects
behavior, command identity, state mutation, locks, Recovery, Export, Copy,
Resume, Final, Reopen, or another contract, stop and decide the new Prompt
Version before editing.

Repository-only changes may be released without new Mode files when they do
not change the Prompt contract. For example, a repository release `v1.0.1`
may still use `Prompt Version: v1.0` for all 35 existing tuples.

## Translation parity rule

If a contract changes in one language, the change must either:

- be synchronized across all five languages with semantic parity checks; or
- be explicitly classified as localization-only, with evidence that behavior,
  command identity, state semantics, locks, and recovery behavior did not
  change.

No language may silently become a new source of truth. RU is not an excuse to
skip parity, and an English or other localized correction must not be promoted
to a contract change without the version decision above.

## Emergency fix path

An emergency fix may shorten review coordination, but it does not bypass the
system contracts:

1. Record the incident, affected tuple, observed evidence, and immediate risk.
2. Preserve Reality First and exact version pinning; do not guess missing
   state or select a `latest` substitute.
3. Apply the smallest reviewed fix or an explicit Recovery/Fallback response.
4. Run the applicable local QA, GitHub Actions, and semantic/parity checks.
5. Update the changelog and document whether a new Prompt Version or patch
   repository release is required.
6. Commit through review as soon as practical and publish only from the exact
   reviewed commit.
7. Never force-push, move/delete a published tag, or silently mutate a running
   project’s pinned tuple.

Emergency handling is a timing exception, not a semantics exception.

## Review and release gates

Before merge, the pull request must state the classification, files changed,
affected tuples, backward-compatibility result, QA performed, and whether a
release is required. The maintainer must verify:

- `scripts/qa.py` passes locally;
- the `Repository QA` GitHub Actions check passes;
- the canonical registry and Mode matrix remain consistent;
- translations and user-facing command labels remain synchronized where
  required;
- no silent fallback, upgrade, or downgrade was introduced;
- no secrets, private paths, or private Project Export data are included;
- the changelog records migration or breaking behavior when applicable.

Merge does not itself create a tag. A release, when required, follows
`system/RELEASE-WORKFLOW.md`: tag the exact reviewed commit, publish matching
notes, and perform external verification. Existing v1.0 tags and releases
remain untouched.

## Maintainer decision rule

When classification is ambiguous, choose the stricter path: treat a possible
contract change as semantic until the evidence proves otherwise, use Recovery
instead of guessing, and require the relevant version, parity, and adversarial
checks. This keeps the published system predictable without blocking ordinary
documentation or tooling maintenance.
