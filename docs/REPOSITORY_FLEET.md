# MemeBank repository fleet

**Observed:** August 5, 2026  
**Tracking:** DEN-1004, DEN-1005, DEN-1043, DEN-319  
**GitHub Project:** [memebank-project](https://github.com/orgs/memebank/projects/1)  
**Linear:** [MemeBank](https://linear.app/denman/project/memebank-3db5f5cc7452)

This document distinguishes repositories that exist in GitHub from the reviewed canonical targets. A plan, source carrier, local archive, or coordinator commit is not remote-publication evidence.

## Live inventory

The organization currently contains these repositories:

| Repository | Visibility | Default branch | Disposition |
|---|---|---|---|
| `.github` | public | `main` | canonical organization governance |
| `mbk-api` | private | `master` | preserve while TypeScript API responsibilities migrate |
| `mbk-ocr-api` | private | `master` | preserve as legacy OCR/analysis service and migration proving ground |
| `mbk-pwa` | private | `master` | preserve while client surfaces migrate |
| `mbk-rest-api` | private | `master` | preserve while canonical Rust API composition lands |
| `mbk-scripts` | private | `master` | inventory and classify automation before consolidation |
| `memebanc-blog` | private | `master` | preserve history; replace only through an explicit migration |
| `stop-billing` | private | `master` | preserve until billing-control ownership is explicitly reassigned |

The misspelled `memebanc-blog` name is recorded as observed history. It is not silently renamed or deleted.

## Canonical targets

The reviewed source-v2 fleet contains thirteen repositories:

1. `.github`
2. `mb-interfaces`
3. `mb-clients`
4. `mb-cli`
5. `memebank-api-server.rs`
6. `memebank-web-server.rs`
7. `memebank-media-worker.rs`
8. `memebank-flutter`
9. `mb-infra`
10. `memebank.github.io`
11. `memebank-mcp-server.rs`
12. `memebank-e2e`
13. `memebank-monorepo`

`.github` is intentionally public so GitHub can render the organization profile. The other canonical targets default to private. `mb-infra` is the sole canonical infrastructure repository; `memebank-infra` is forbidden.

## Publication order and invariants

Publish contract and leaf repositories before orchestration:

1. governance and interfaces;
2. clients and CLI;
3. API, web, media-worker, Flutter, infrastructure, marketing, MCP, and E2E repositories;
4. `memebank-monorepo` last, after every child commit is reachable.

Each new repository requires:

- exact organization and repository identity;
- intended visibility and `main` default branch;
- a reviewed baseline branch and pull request rather than an undocumented final push;
- required CI, CODEOWNERS, branch/ruleset, workflow-permission, secret, Dependabot, and security settings;
- first remote commit, baseline PR, merge SHA, checks, and repository ID recorded in Linear and the GitHub Project;
- no overwrite of a nonempty remote unless a separately reviewed migration proves ancestry and desired state.

The monorepo must pin exact child commits. It must not import infrastructure or CLI merely for convenience when the approved topology excludes them, and it must not hide duplicate source copies behind Git submodules.

## Legacy migration policy

Existing repositories continue to receive security and compatibility fixes. Migration to canonical targets is incremental:

- preserve useful behavior, tests, migrations, documentation, and audit history;
- extract versioned contracts before implementation replacement;
- run old and new paths in conformance or shadow mode where practical;
- document data, deployment, and ownership cutovers;
- archive or deprecate only after replacement evidence and rollback are complete.

A semantic merge reconstructs the intent of both branches. It does not resolve conflicts by selecting all of `ours`, all of `theirs`, current, or incoming.

## Completion evidence

DEN-1005 is complete only when all thirteen targets have verified remote identities and the intended baseline commits. DEN-1043 additionally requires organization and repository governance to be applied and tested. DEN-319 requires the approved short-lived publishing identity and audit trail. The presence of `.github` and the legacy repositories does not satisfy those acceptance criteria.
