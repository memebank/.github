# MemeBank repository fleet

**Observed:** August 7, 2026  
**Tracking:** DEN-1004, DEN-1005, DEN-1043, DEN-319  
**GitHub Project:** [memebank-project](https://github.com/orgs/memebank/projects/1)  
**Linear:** [MemeBank](https://linear.app/denman/project/memebank-3db5f5cc7452)

This document distinguishes repositories that exist in GitHub from reviewed canonical targets. A plan, source carrier, local archive, generated Git bundle, or coordinator commit is not remote-publication evidence.

## Live inventory

The organization currently contains these recovery-relevant and legacy repositories:

| Repository | Visibility | Default branch | Disposition |
|---|---|---|---|
| `.github` | public | `main` | canonical organization governance; newer than the recovered bootstrap |
| `memebank-e2e` | private | `main` | canonical E2E repository; archived Rust matrix is being semantically recovered through PR #3 |
| `mbk-cli` | private | `main` | empty naming collision; not a substitute for canonical `mb-cli` |
| `mbk-api` | private | `master` | preserve while TypeScript API responsibilities migrate |
| `mbk-ocr-api` | private | `master` | preserve as legacy OCR/analysis service and migration proving ground |
| `mbk-pwa` | private | `master` | preserve while client surfaces migrate |
| `mbk-rest-api` | private | `master` | preserve while canonical Rust API composition lands |
| `mbk-scripts` | private | `master` | inventory and classify automation before consolidation |
| `memebanc-blog` | private | `master` | preserve history; replace only through an explicit migration |
| `stop-billing` | private | `master` | preserve until billing-control ownership is explicitly reassigned |

The misspelled `memebanc-blog` name is recorded as observed history. It is not silently renamed or deleted. The empty `mbk-cli` remote is also preserved until an explicit rename/archive decision; publication work must still create `mb-cli` under the current fleet contract.

## Current canonical targets

The original July 31 source fleet contained thirteen repositories. The August 6 desktop decision superseded the generated `memebank-flutter` remote name with `mbk-flutter` and added a separate native Rust desktop target, producing this current fourteen-target family:

1. `.github`
2. `mb-interfaces`
3. `mb-clients`
4. `mb-cli`
5. `memebank-api-server.rs`
6. `memebank-web-server.rs`
7. `memebank-media-worker.rs`
8. `mbk-flutter`
9. `mbk-desktop.rs`
10. `mb-infra`
11. `memebank.github.io`
12. `memebank-mcp-server.rs`
13. `memebank-e2e`
14. `memebank-monorepo`

`.github` is intentionally public so GitHub can render the organization profile. `memebank.github.io` is intended to be public for the reviewed Pages deployment. Other canonical targets default to private unless a reviewed visibility decision says otherwise. `mb-infra` is the sole canonical infrastructure repository; `memebank-infra` is forbidden.

### Recovered-source mapping

- The sealed `memebank-flutter` source commit is a migration source for `mbk-flutter`; do not create both remotes.
- No generated `mbk-desktop.rs` source tree was found; do not manufacture an empty placeholder merely to satisfy inventory.
- The sealed `memebank.github.io` source is older than the current staging tree under `.github/marketing-site`; migrate the newer staging tree.
- The sealed `memebank-e2e` history must be merged semantically into the live repository, not force-pushed.

See [`RECOVERY_2026-08-07.md`](RECOVERY_2026-08-07.md) for exact source commits, archive digest, validation evidence, and the publication blocker.

## Publication order and invariants

Publish contract and leaf repositories before orchestration:

1. governance and interfaces;
2. clients and CLI;
3. API, web, media-worker, Flutter, infrastructure, marketing, MCP, and E2E repositories;
4. the native Rust desktop repository only when a real buildable source tree exists;
5. `memebank-monorepo` last, after every referenced child commit is reachable.

Each new repository requires:

- exact organization and repository identity;
- intended visibility and `main` default branch;
- a reviewed baseline branch and pull request rather than an undocumented final push;
- required CI, CODEOWNERS, ruleset/branch protection, workflow permissions, secret policy, Dependabot, and security settings;
- first remote commit, baseline PR, merge SHA, checks, and repository ID recorded in Linear and the GitHub Project;
- no overwrite of a nonempty remote unless a separately reviewed migration proves ancestry and desired state; and
- credential-free publication logs and remotes.

The monorepo must pin exact reachable child commits. It must not hide duplicate source copies behind submodules, and it must not import infrastructure or CLI merely for convenience when the approved topology excludes them.

## Legacy migration policy

Existing repositories continue to receive security and compatibility fixes. Migration to canonical targets is incremental:

- preserve useful behavior, tests, migrations, documentation, and audit history;
- extract versioned contracts before implementation replacement;
- run old and new paths in conformance or shadow mode where practical;
- document data, deployment, and ownership cutovers;
- archive or deprecate only after replacement evidence and rollback are complete.

A semantic merge reconstructs the intent of both branches. It does not resolve conflicts by selecting all of `ours`, all of `theirs`, current, or incoming.

## Completion evidence

DEN-1005 is complete only when every approved target has a verified remote identity and intended baseline commit. DEN-1043 additionally requires organization and repository governance to be applied and tested. DEN-319 requires the approved short-lived publishing identity and audit trail.

Current partial evidence:

- `.github` is live;
- `memebank-e2e` is live and recovery PR #3 carries the archived Rust matrix on top of newer process tests;
- the remaining recovered source histories are sealed and publish-ready but their canonical remotes do not yet exist;
- `mbk-desktop.rs` remains planned without generated source; and
- `mbk-cli` is an empty collision, not canonical completion.

The presence of source archives, `.github`, `memebank-e2e`, `mbk-cli`, or the legacy repositories does not satisfy the remaining publication acceptance criteria.
