# Desktop application allocation

Verified **2026-08-06**.

MemeBank is allocated a paired desktop media-library product:

- Rust: [`memebank/mbk-desktop.rs`](https://github.com/memebank/mbk-desktop.rs) — **planned**, not yet verified as a published repository.
- Flutter: [`memebank/mbk-flutter`](https://github.com/memebank/mbk-flutter) — **planned**, not yet verified as a published repository.

The `mbk-*` naming is canonical for this pair unless an explicit ADR changes it. The planned URLs are allocation targets, not proof that either remote exists.

## Why both Rust and Flutter remain active

The two applications will be first-class side-by-side implementations so MemeBank can compare media-grid performance, local indexing, OS integration, accessibility, mobile reuse, developer velocity, packaging, security, and long-term maintenance with the same library features.

Every desktop-facing feature must be planned against both repositories, share acceptance criteria and privacy-safe fixtures, and normally update both. A one-sided change requires a documented no-change rationale and parity gap.

## Rust desktop kit: Tauri 2 without React

**Selected strategy:** Tauri 2.

**WebView policy:** allowed for this product.

**Frontend policy:** no React, JSX, React-derived stack, Vue, or Svelte. Use vanilla HTML, CSS, and TypeScript. HTMX is allowed for authenticated server-driven fragments where it reduces client complexity. Rust/Tauri commands own filesystem access, indexing, OCR/vision queues, encryption, secure storage, and privileged operations; do not expose an unauthenticated loopback API.

Media grids, drag/drop, previews, metadata editing, search, and local/remote synchronization fit a minimal HTML UI, while Rust owns performance-sensitive indexing and security boundaries.

The Rust repository must contain `docs/DESKTOP_TOOLKIT.md` covering Tauri 2 version policy, CSP/capabilities, frontend restrictions, command boundaries, media/file permissions, deep links, tests, packaging, and Flutter companion.

## HTTPS-first deep linking

Canonical form:

```text
https://<verified-memebank-owned-host>/open/<route>?<bounded-query>
```

Fallback scheme:

```text
memebank://<route>?<bounded-query>
```

Routes must be defined in the MemeBank interfaces package and shared by Rust, Flutter, clients, Cliptown interop, and browser fallback pages.

Required behavior:

- use `tauri-plugin-deep-link` plus `tauri-plugin-single-instance`;
- support cold-start and already-running delivery;
- validate the exact host, route, library/item/collection identifiers, action, and bounded query parameters;
- never place private media, OCR text, embeddings, storage credentials, encryption keys, bearer tokens, or personal metadata in URLs;
- use short-lived, one-time, audience-bound codes for shares, imports, authentication, and Cliptown handoffs;
- require confirmation before importing or revealing external media; and
- test macOS, Windows, Linux, Android, and iOS app/universal links plus browser fallback.

## Product boundary

Both implementations should support semantic parity for drag/drop and bulk import, local/offline indexing, OCR/vision queues, embeddings, tags/search, storage-provider connectors, encryption boundaries, duplicate detection, export/share flows, Cliptown interoperability, and deep links.

Shared schemas, clients, route fixtures, privacy-safe sample media, metadata formats, and conformance tests must be versioned deliberately.

## Repository creation requirements

Both repositories must begin as buildable scaffolds, not placeholders. The Rust repo must include `docs/DESKTOP_TOOLKIT.md`, reciprocal README/AGENTS/PR guidance, native CI/package skeletons, smoke tests, privacy controls, and shared contract fixtures.

Central toolkit assignments: [`rust-desktop-strategies.md`](https://github.com/ORESoftware/project-registry/blob/main/docs/rust-desktop-strategies.md).

## Project routing

- GitHub Project: [`memebank-project` — Project 1](https://github.com/orgs/memebank/projects/1)
- Linear project: `memebank`
- Central registry: [`approved-private-registry`](private-registry://canonical/registry/desktop-applications.json)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Repository creation, naming changes, toolkit/frontend changes, deep-link changes, transfers, archival, or platform-status changes must update this document, the central registry/strategy, Linear, and both companion repositories in the same delivery.
