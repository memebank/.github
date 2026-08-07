# MemeBank unrelated-history collision archives — 2026-08-07

## Purpose

The canonical MemeBank fleet was published successfully without requiring alternate names. After that canonical publication completed, the user explicitly requested that every already-created repository with an unrelated history also receive a complete source publication under the `<name>-2` rule.

These `-2` repositories are **audited archival/collision histories**, not canonical replacements:

- normal feature development continues in the canonical repository names;
- `memebank-monorepo` pins canonical children, not these archives;
- no canonical branch was force-pushed or rewritten;
- no two unrelated histories were falsely represented as sharing ancestry;
- each archive preserves its recovery/provenance commits; and
- source was published through reviewed branches and pull requests where the pre-created collision repository contained only provenance metadata.

## Complete archive inventory

| Archive repository | Publication evidence | Current disposition |
|---|---|---|
| [`memebank/.github-2`](https://github.com/memebank/.github-2) | exact sealed governance source at `fa12eacab448a6e7dc16c17491efa1157d1992cb`; source tree `6f885dadcfcd4192c7c10e64beccd91ea695bbd7` | complete governance archive |
| [`memebank/mb-interfaces-2`](https://github.com/memebank/mb-interfaces-2) | exact recovered source at `916c0224ee400f863f1b631469b6afe629fd8e80`; source tree `93f6a89d832d88b4e880318fdd8f0cba1b0153ac` | complete contract archive |
| [`memebank/mb-clients-2`](https://github.com/memebank/mb-clients-2) | exact recovered source at `20d2a471405e160a6e1da7bb33e13abfe81c7ccd`; source tree `a3fe68a687d5303e016670b0827c7cb316016f2d` | complete SDK archive |
| [`memebank/mb-cli-2`](https://github.com/memebank/mb-cli-2) | exact recovered source at `563b8a56bc44d2b057b68f392dec1fab2c27fdbf`; source tree `ae8295c844810c39e0938046731e81c305826a52` | complete CLI archive |
| [`memebank/mb-infra-2`](https://github.com/memebank/mb-infra-2) | exact recovered source at `cf305147acecad52536541ae35b93379bf755eb3`; source tree `c08f941acaf6a4761f418a74fb675f492b9add39` | complete infrastructure archive |
| [`memebank/memebank-api-server.rs-2`](https://github.com/memebank/memebank-api-server.rs-2) | [PR #1](https://github.com/memebank/memebank-api-server.rs-2/pull/1), merged at `204465333fc93f3b98566d7eb7395180695ba8ea` | complete recovered Rust API tree plus provenance |
| [`memebank/memebank-web-server.rs-2`](https://github.com/memebank/memebank-web-server.rs-2) | [PR #1](https://github.com/memebank/memebank-web-server.rs-2/pull/1), merged at `8950aa8de2a1e6262246bfb368ec2920cae0f4b2` | complete recovered Maud/Axum web tree plus provenance |
| [`memebank/memebank-media-worker.rs-2`](https://github.com/memebank/memebank-media-worker.rs-2) | [PR #1](https://github.com/memebank/memebank-media-worker.rs-2/pull/1), merged at `4f0b1dee258ba91db2a3d7c1accfc75178ec95aa` | complete recovered media-worker tree plus provenance |
| [`memebank/memebank-flutter-2`](https://github.com/memebank/memebank-flutter-2) | [PR #1](https://github.com/memebank/memebank-flutter-2/pull/1), merged at `3bb17fe5a4d3b1adae167f3cced122396b3d52d3` | complete recovered Flutter tree plus provenance; canonical app remains `mbk-flutter` |
| [`memebank/memebank-mcp-server.rs-2`](https://github.com/memebank/memebank-mcp-server.rs-2) | [PR #1](https://github.com/memebank/memebank-mcp-server.rs-2/pull/1), merged at `65669a7f054bc1c1e09e8c53097944f76cf62249` | complete recovered read-only MCP tree plus provenance |
| [`memebank/memebank-monorepo-2`](https://github.com/memebank/memebank-monorepo-2) | [PR #1](https://github.com/memebank/memebank-monorepo-2/pull/1), merged at `835f4606c7f45ce6111bfa9e503e93401b7e9399` | complete recovered coordination tree plus provenance; canonical monorepo remains authoritative |
| [`memebank/memebank-e2e-2`](https://github.com/memebank/memebank-e2e-2) | [PR #1](https://github.com/memebank/memebank-e2e-2/pull/1), merged at `5254b6748b8cfa8dca11e4cb21b424b7a76f7d1f` | mirror of the current semantically reconciled canonical E2E tree plus provenance |
| [`memebank/memebank.github.io-2`](https://github.com/memebank/memebank.github.io-2) | [PR #1](https://github.com/memebank/memebank.github.io-2/pull/1), merged at `d7409b4398bb765c62839df110c3c0b14d7a60fb` | mirror of the newer canonical Astro site, not the stale July snapshot, plus provenance |

## Desktop exception

No `mbk-desktop.rs-2` archive was created. `memebank/mbk-desktop.rs` was a new substantive canonical GPUI implementation rather than a recovered repository facing an unrelated-history collision. Creating an empty or duplicate `-2` desktop repository would add ambiguity without preserving any missing source.

## Validation boundary

The recovered local source package was checked for JSON, TOML, YAML, shell syntax, repository topology, and credential-like content before publication. Executable file modes were restored for the Flutter platform bootstrap, monorepo orchestration scripts, and E2E agent check. GitHub pull requests preserve the publication evidence and reviewable diffs.

GitHub Actions status is tracked independently. Archive publication completion means the source is reachable in GitHub with provenance; it does not by itself certify every runtime, package, signing identity, supported platform, or production deployment.

## Security

The supplied GitHub PAT and Linear token were used only through ephemeral authenticated execution paths. They were not committed, embedded in remotes, added to issues or documents, or copied into source files. Repository records contain source identities and merge evidence, not secret values.
