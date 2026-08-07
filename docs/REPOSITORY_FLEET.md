# MemeBank repository fleet

**Verified:** August 7, 2026  
**Tracking:** DEN-1004, DEN-1005, DEN-1043, DEN-319, DEN-1011, DEN-1018, DEN-2469  
**GitHub Project:** [memebank-project](https://github.com/orgs/memebank/projects/1)  
**Linear:** [MemeBank](https://linear.app/denman/project/memebank-3db5f5cc7452)

Repository recovery and first publication are complete. The authoritative canonical completion record is [`.github#26`](https://github.com/memebank/.github/issues/26). This document records the current canonical fleet and distinguishes it from legacy repositories, unused naming placeholders, and the later user-requested unrelated-history `-2` archives.

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

## Canonical collision policy and later archive publication

The canonical recovery itself did not require a `-2` name: every canonical destination was empty, created by the recovery publisher, or demonstrably contained the same product source with newer reviewed additions. No nonempty canonical repository was force-pushed.

After canonical completion, the user explicitly requested that the separately created unrelated-history collision repositories also receive complete source publication. Those repositories now exist as **archives**, not alternative canonical development targets. Their exact source identities, pull requests, and merge commits are recorded in [`COLLISION_ARCHIVES_2026-08-07.md`](COLLISION_ARCHIVES_2026-08-07.md).

For all future recovery work:

- use the canonical name when the destination is empty, missing, or demonstrably shares the recovered lineage;
- preserve and semantically reconcile newer work when both histories represent the same product;
- when an occupied name is an unrelated project with no shared lineage, create `<name>-2`, publish the complete source rather than a metadata-only placeholder, and record the mapping in this document, Linear, and the recovery ledger;
- keep `-2` repositories outside canonical monorepo pins unless a later explicit migration changes authority;
- never resolve a conflict by blindly taking all of `ours` or all of `theirs`; and
- never force-push a nonempty canonical remote merely to reproduce an archived commit SHA.

## Noncanonical placeholders, archives, and legacy repositories

The repositories `mbk-cli`, `mbk-interfaces`, `mbk-clients`, and `mbk-lib` are not substitutes for the canonical `mb-cli`, `mb-interfaces`, and `mb-clients` repositories. They remain separate until a reviewed naming, migration, or archival decision.

The published `-2` repositories preserve unrelated/recovery histories and complete source snapshots. They are not canonical package, deployment, or feature-development targets. Normal product work remains in the canonical fleet above.

Legacy repositories such as `mbk-api`, `mbk-rest-api`, `mbk-ocr-api`, `mbk-pwa`, `mbk-scripts`, `memebanc-blog`, and `stop-billing` retain their history while behavior is migrated deliberately. Existing security and compatibility fixes may continue there until the corresponding cutover is complete.

## Publication invariants

- Contract and leaf repositories are published before orchestration repositories.
- `memebank-monorepo` is published last and pins reachable canonical child commits.
- `.github` is the public organization-governance exception; product repositories default to private unless a reviewed visibility decision says otherwise.
- Repository remotes, publication logs, pull requests, and ledgers contain no PATs, Linear tokens, signing keys, or other credentials.
- Archive publication preserves provenance but does not imply production readiness, package signing, supported-platform qualification, or deployment activation.
- CI, governance, packaging, signing, production activation, migrations, provider qualification, accessibility, performance, observability, and failure drills remain independently tracked product-delivery work.

See [`RECOVERY_2026-08-07.md`](RECOVERY_2026-08-07.md) for source-carrier provenance and [`COLLISION_ARCHIVES_2026-08-07.md`](COLLISION_ARCHIVES_2026-08-07.md) for the post-completion archive publication.
