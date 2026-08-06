# MemeBank desktop applications

Verified **2026-08-06**.

## Required pair

- Rust: [`memebank/mbk-desktop.rs`](https://github.com/memebank/mbk-desktop.rs) — **planned**, not yet verified as published.
- Flutter: [`memebank/mbk-flutter`](https://github.com/memebank/mbk-flutter) — **planned**, not yet verified as published.

The `mbk-*` naming is canonical. Do not mark either implementation live until the remote, native build, packaging, performance tests, and supported-platform matrix are verified.

## Rust desktop kit: GPUI, fully native

The Rust application uses **GPUI**. The prior Tauri/WebView assignment is superseded.

- Embedded WebViews are prohibited.
- Rust owns local indexing, OCR/vision queues, embeddings, metadata, storage connectors, encryption, secure storage, persistence, Cliptown handoffs, deep-link parsing, and privileged filesystem operations.
- GPUI owns native image grids, virtualized collections, thumbnails/previews, keyboard navigation, selection, drag/drop surfaces, custom rendering, windowing, and low-latency interaction.
- Image decode, thumbnail, cache, and GPU/upload work must use bounded pipelines and explicit memory/performance budgets.

This strategy prioritizes high-performance native image rendering, large media libraries, fast scrolling and selection, direct OS drag/drop/clipboard integration, and low-latency interoperability with Cliptown.

The future Rust repository must contain `docs/DESKTOP_TOOLKIT.md` covering the GPUI version policy, no-WebView rule, image/rendering architecture, memory/performance budgets, filesystem and security boundaries, deep links, Cliptown interop, packaging, platform tests, and Flutter companion.

## Parallel Rust and Flutter development

The Rust and Flutter applications are first-class side-by-side implementations. They are developed with the same product features to compare native image/rendering performance, local integration, accessibility, Flutter mobile reuse, developer velocity, packaging, security, and long-term maintenance.

Every desktop-facing feature must inspect both repositories, share acceptance criteria and privacy-safe fixtures, and normally update both. A one-sided change requires an explicit no-change rationale and parity gap. The future `mbk-desktop.rs` README, `AGENTS.md`, pull-request template, and `docs/DESKTOP_TOOLKIT.md` must state this rule prominently.

## HTTPS-first deep links

Canonical route family:

```text
https://<verified-memebank-owned-host>/open/<route>?<bounded-query>
```

Fallback scheme:

```text
memebank://<route>?<bounded-query>
```

Rust and Flutter must consume the same versioned route types and fixtures from the MemeBank interfaces package.

Initial route families may include libraries, collections, media items, searches, import reviews, shares, storage connectors, Cliptown handoffs, and authenticated notifications.

Required behavior:

- cold-start and already-running/single-instance delivery;
- exact host, route/version, library/item/collection identifiers, action, and bounded-query validation;
- authenticated resume and browser fallback;
- replay, expiry, ownership, storage-provider, and unsafe-return validation;
- explicit confirmation before import, reveal, export, deletion, connector changes, or external-file access; and
- macOS, Windows, Linux, Android, and iOS tests.

Private media, image bytes, OCR text, embeddings, storage credentials, encryption keys, bearer tokens, local absolute paths, or personal metadata are prohibited in URLs. Use short-lived, single-use, audience-bound codes for shares, imports, authentication, and Cliptown handoffs.

## Native MemeBank–Cliptown interoperability

MemeBank and Cliptown must share a versioned local image-transfer contract across all four Rust/Flutter applications.

- Prefer OS drag/drop, clipboard provider formats, shared file references, and authenticated local manifests rather than encoding media in URLs.
- Deep links may contain only bounded identifiers or one-time handoff codes.
- Validate MIME type, size, origin, file identity, destination, user intent, and access rights before import.
- Support copy, move, reference, pin, and collection-add semantics explicitly; never infer destructive behavior.
- Use privacy-safe golden images and round-trip/failure fixtures across `mbk-desktop.rs`, `mbk-flutter`, `cliptown-desktop.rs`, and `cliptown-flutter`.
- Preserve original files by default; destructive transfer requires explicit confirmation and durable audit evidence.

## Product boundary

Both MemeBank implementations should converge on:

- drag/drop and bulk import;
- high-performance native image grids and previews;
- local/offline indexing, OCR/vision queues, embeddings, tags, and search;
- storage-provider connectors, encryption boundaries, duplicate detection, export/share flows, and Cliptown interop;
- caching, memory budgets, background jobs, progress/recovery, notifications, and deep links;
- schemas, generated clients, route fixtures, privacy-safe sample media, metadata formats, and conformance tests.

## Project routing

- GitHub Project: [`memebank-project` — Project 1](https://github.com/orgs/memebank/projects/1)
- Linear project: `memebank`
- Central registry: [`desktop-applications.json`](https://github.com/ORESoftware/project-registry/blob/main/registry/desktop-applications.json)
- Toolkit strategy: [`rust-desktop-strategies.md`](https://github.com/ORESoftware/project-registry/blob/main/docs/rust-desktop-strategies.md)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, toolkit changes, deep-link or Cliptown-interop changes, renames, transfers, archival, or platform-status changes must update this document, Linear, the central registry/strategy, and both companion repositories together.
