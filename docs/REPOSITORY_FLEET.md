# MemeBank repository fleet

**Verified:** August 7, 2026  
**Tracking:** DEN-1004, DEN-1005, DEN-1043, DEN-319, DEN-1011, DEN-1018, DEN-2469  
**GitHub Project:** [memebank-project](https://github.com/orgs/memebank/projects/1)  
**Linear:** [MemeBank](https://linear.app/denman/project/memebank-3db5f5cc7452)

Repository recovery and first publication are complete. The authoritative completion record is [`.github#26`](https://github.com/memebank/.github/issues/26). This document records the current canonical fleet and distinguishes it from legacy repositories and unused naming placeholders.

## Canonical fleet

| Repository | Visibility | State | Verified revision or disposition |
|---|---|---|---|
| `.github` | public | live | organization governance; reconciled additively |
| `mb-interfaces` | private | live | source-v2 head `c860e0ac8281a10952d31e7274813e8bfc0af781` |
| `mb-clients` | private | live | source-v2 head `ee81a0eedba4c44a2819023d0bb7d1311599fba2` |
| `mb-cli` | private | live | source-v2 head `3455f25e96a8cfc65958b5048f8b03074c67fb58` |
| `memebank-api-server.rs` | private | live | source-v2 head `fe28c76f2ae634fea8216eb8992bd6cfabdc13cb` |
| `memebank-web-server.rs` | private | live | source-v2 head `d355504bf49551ee6f4360a96d0200c4e581c3e9` |
| `memebank-media-worker.rs` | private | live | source-v2 head `7b228d6e1c0edffb15580fec4bba98bcd7fa6df5` |
| `mbk-flutter` | private | live | renamed from `memebank-flutter` with repository ID and Git history preserved; current verified tree `6beb20cdb65790d4e2890a05b777cc0a9de1efa9` |
| `mbk-desktop.rs` | private | live | substantive native Rust/GPUI source; verified commit `c7e5b9010bb984b6443ae00e5a4a162fc62b4cc5` |
| `mb-infra` | private | live | source-v2 head `95869b2b0709e1b514192aeea6ffc1b70993a224`; `memebank-infra` remains forbidden |
| `memebank.github.io` | private | live | reviewed site source `b693ba989b775b4ea280e75c86a809479d073b80`; visibility remains a separate Pages decision |
| `memebank-mcp-server.rs` | private | live | source-v2 head `192fa6765991c18f061f2d2d67aff6cf3de952f9` |
| `memebank-e2e` | private | live | recovered source attached as audited ancestry while preserving the newer reconciled product tree |
| `memebank-monorepo` | private | live | published last; exact child revisions are pinned and validated |

The final source-v2 publication run reported **13 repositories current, zero failures, and 28 publisher/carrier tests passed**. The desktop extension adds the fourteenth canonical repository, `mbk-desktop.rs`.

## Conflict and ancestry policy

No `-2` repository was required for the recovered fleet. Every occupied canonical target was either created by the recovery publisher or contained the same recovered source lineage with newer reviewed metadata or follow-up work. Recovered blobs were not force-pushed over unrelated history.

For future recovery work:

- use the canonical name when the destination is empty, missing, or demonstrably shares the recovered lineage;
- preserve and semantically reconcile newer work when both histories represent the same product;
- when an occupied name is an unrelated project with no shared lineage, create `<name>-2` and record the mapping in this document, Linear, and the monorepo;
- never resolve a conflict by blindly taking all of `ours` or all of `theirs`;
- never force-push a nonempty canonical remote merely to reproduce an archived commit SHA.

## Noncanonical placeholders and legacy repositories

The empty repositories `mbk-cli`, `mbk-interfaces`, `mbk-clients`, and `mbk-lib` are not substitutes for the canonical `mb-cli`, `mb-interfaces`, and `mb-clients` repositories. They remain unused until a separate reviewed naming or archival decision. Do not duplicate the source fleet into them.

Legacy repositories such as `mbk-api`, `mbk-rest-api`, `mbk-ocr-api`, `mbk-pwa`, `mbk-scripts`, `memebanc-blog`, and `stop-billing` retain their history while behavior is migrated deliberately. Existing security and compatibility fixes may continue there until the corresponding cutover is complete.

## Publication invariants

- Contract and leaf repositories are published before orchestration repositories.
- `memebank-monorepo` is published last and pins reachable child commits.
- `.github` is the public organization-governance exception; product repositories default to private unless a reviewed visibility decision says otherwise.
- Repository remotes and publication logs contain no PATs, Linear tokens, signing keys, or other credentials.
- CI, governance, packaging, signing, production activation, migrations, provider qualification, accessibility, performance, observability, and failure drills remain independently tracked product-delivery work.

See [`RECOVERY_2026-08-07.md`](RECOVERY_2026-08-07.md) for source-carrier provenance and the final recovery verification.
