# MemeBank desktop applications

Verified **2026-08-06/07**.

## Published pair

- Rust: [`memebank/mbk-desktop.rs`](https://github.com/memebank/mbk-desktop.rs) — private, native Rust/GPUI, no WebView; reviewed `main` commit `c7e5b9010bb984b6443ae00e5a4a162fc62b4cc5`.
- Flutter: [`memebank/mbk-flutter`](https://github.com/memebank/mbk-flutter) — private, mobile, mobile web, and desktop; reviewed `main` commit `6beb20cdb65790d4e2890a05b777cc0a9de1efa9`.
- Coordinator: [`memebank/memebank-monorepo`](https://github.com/memebank/memebank-monorepo) — exact paired gitlinks at commit `c4510c6d026c0f3459247063fc877842c363e16f`.

The Flutter repository was renamed from `memebank/memebank-flutter` rather than copied. Repository ID `1326070645`, all Git history, and the sealed source-v2 commit were preserved. The Rust repository has ID `1326085867`.

The `mbk-*` naming is canonical. Packaging, signing, distribution, performance qualification, accessibility review, and the complete supported-platform matrix remain release work; repository publication alone does not certify those items.

## Verified checks

### Rust/GPUI

- stable `rustfmt`;
- Clippy with warnings denied;
- platform-neutral contract tests;
- macOS native GPUI compile check with `gpui = "=0.2.2"`;
- strict deep-link and ClipTown command validation;
- canonical singular asset route plus legacy plural migration support.

### Flutter

- vendored `mb-interfaces` Dart package verified against approved commit `c860e0ac8281a10952d31e7274813e8bfc0af781` and fixed SHA-256 hashes;
- `flutter pub get`, `flutter analyze`, and `flutter test` green;
- no repository-scoped cross-private checkout dependency in CI;
- canonical singular asset deep links emitted from clipboard metadata.

### Monorepo

- old `apps/memebank-flutter` gitlink removed;
- exact `apps/mbk-flutter` and `apps/mbk-desktop.rs` gitlinks enforced by `desktop-pins.json` and `scripts/validate-workspace.sh`;
- workspace validation green.

## Rust desktop kit: GPUI, fully native

The Rust application uses **GPUI**. The prior Tauri/WebView assignment is superseded.

- Embedded WebViews are prohibited.
- Rust owns local indexing, OCR/vision queues, embeddings, metadata, storage connectors, encryption, secure storage, persistence, ClipTown handoffs, deep-link parsing, and privileged filesystem operations.
- GPUI owns native image grids, virtualized collections, thumbnails/previews, keyboard navigation, selection, drag/drop surfaces, custom rendering, windowing, and low-latency interaction.
- Image decode, thumbnail, cache, and GPU/upload work must use bounded pipelines and explicit memory/performance budgets.

This strategy prioritizes high-performance native image rendering, large media libraries, fast scrolling and selection, direct OS drag/drop/clipboard integration, and low-latency interoperability with ClipTown.

## Parallel Rust and Flutter development

The Rust and Flutter applications are first-class side-by-side implementations. They need not remain feature-for-feature identical, but every change involving imports, search, auth, API models, clipboard metadata, sharing, deep links, offline state, storage providers, or background processing must review both repositories. A one-sided change requires an explicit rationale, test evidence, and compatibility or rollback path.

Shared data shapes are owned by `memebank/mb-interfaces`; transport behavior is owned by `memebank/mb-clients`; cross-application fixtures belong in `memebank/memebank-e2e`. Neither UI repository is the canonical schema owner.

## Deep links

Canonical custom-scheme routes:

```text
memebank://library
memebank://search?q=<bounded-query>
memebank://asset/<asset-id>
memebank://import?uri=<absolute-uri>
```

Allowlisted HTTPS app links may use the same route grammar under `/app`. The historical `memebank://assets/<asset-id>` route is accepted during migration, but new payloads emit the singular `asset` form.

Required behavior includes cold-start and already-running delivery, exact host/route validation, bounded identifiers and queries, authenticated resume, replay/expiry checks, and explicit confirmation before import, reveal, export, deletion, connector changes, or external-file access.

Private media, OCR text, embeddings, storage credentials, encryption keys, bearer tokens, local absolute paths, and personal metadata are prohibited in URLs. Use short-lived, single-use, audience-bound codes for shares, imports, authentication, and ClipTown handoffs.

## Native MemeBank–ClipTown interoperability

- Prefer OS drag/drop, clipboard provider formats, shared file references, and authenticated local manifests rather than encoding media in URLs.
- Deep links may contain only bounded identifiers or one-time handoff codes.
- Validate MIME type, size, origin, file identity, destination, user intent, and access rights before import.
- Support copy, move, reference, pin, and collection-add semantics explicitly; never infer destructive behavior.
- Use privacy-safe golden images and round-trip/failure fixtures across `mbk-desktop.rs`, `mbk-flutter`, `cliptown-desktop.rs`, and `cliptown-flutter`.
- Preserve original files by default; destructive transfer requires explicit confirmation and durable audit evidence.

## Project routing

- GitHub Project: [`memebank-project` — Project 1](https://github.com/orgs/memebank/projects/1)
- Linear project: `memebank`
- Fleet recovery: `DEN-1043`
- Desktop rollout: `DEN-2469`
- Canonical fleet evidence: [`.github#26`](https://github.com/memebank/.github/issues/26)

Repository creation, toolkit changes, deep-link or ClipTown-interop changes, renames, transfers, archival, and platform-status changes must update this document, Linear, the monorepo pins, and both companion repositories together.
