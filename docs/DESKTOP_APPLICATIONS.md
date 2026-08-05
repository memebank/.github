# Desktop application allocation

Verified **2026-08-05**.

MemeBank is allocated a paired native desktop media-library product:

- Rust: [`memebank/mbk-desktop.rs`](https://github.com/memebank/mbk-desktop.rs) — **planned**, not yet verified as a published repository.
- Flutter: [`memebank/mbk-flutter`](https://github.com/memebank/mbk-flutter) — **planned**, not yet verified as a published repository.

Earlier planning has also used `memebank-flutter`. The current registry allocation is `mbk-flutter`; naming must be resolved before repository creation. A rename or alternate choice must update this document, the central registry, Linear, and both companion references together.

The planned URLs are allocation targets, not proof that either remote exists. Do not mark an implementation live until the repository, native targets, tests, packaging, and supported-platform matrix are verified.

## Product boundary

Both implementations should support semantic parity for drag-and-drop and bulk media import, local/offline indexing, OCR and vision-analysis queues, tags and search, storage-provider connectors, encryption boundaries, duplicate detection, export/share flows, and Cliptown interoperability through explicit APIs or SDKs.

The Rust and Flutter implementations remain independently buildable, testable, releasable applications. Shared schemas, clients, fixtures, sample media, metadata formats, and conformance tests should be versioned deliberately.

## Feature-delivery rule

For every desktop-facing feature:

1. inspect both allocated repositories before deciding scope;
2. define shared acceptance criteria and identify affected contracts and fixtures;
3. create or update work for both implementations, or record an explicit no-change rationale;
4. test and report Rust and Flutter status separately; and
5. keep reciprocal repository references, storage/security assumptions, and platform matrices current.

## Project routing

- GitHub Project: [`memebank-project` — Project 1](https://github.com/orgs/memebank/projects/1)
- Linear project: `memebank`
- Central registry: [`ORESoftware/project-registry`](https://github.com/ORESoftware/project-registry/blob/main/registry/desktop-applications.json)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, naming resolution, renames, transfers, archival, or platform-status changes must update this document, the central registry, the Linear project, and both companion repositories in the same delivery.
