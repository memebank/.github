# DEN-2259 — MemeBank shared-auth and ClipTown activation

Linear `DEN-2259` is the authoritative cross-organization delivery issue. MemeBank owns the product action boundary and composition of official shared-auth and ClipTown SDKs. It does not own factor verification or ClipTown transfer persistence.

## Non-negotiable architecture

MemeBank consumes authentication and high-assurance state only through shared-auth. It must not:

- import or call a 3FA service client;
- validate a 3FA-specific proof, token, header, challenge, or callback;
- probe whether 3FA or ClipTown is installed;
- invoke a mobile deep link, platform intent, app extension, local IPC, or loopback service;
- share a database, object-store credential, or service credential with ClipTown;
- monitor the clipboard or silently fall back to clipboard transport when the API is unavailable.

MemeBank and ClipTown interoperate through the versioned ClipTown HTTPS API and official SDKs. The flow must work from web, desktop, CLI, worker, and server contexts with both phone apps absent. Native **Copy** remains an explicit foreground operating-system feature, not the integration transport.

## Active delivery chain

| Order | Repository item | Purpose | MemeBank dependency |
|---:|---|---|---|
| 1 | `shared-auth/shared-auth-server.rs#38` | Complete delegated introspection lineage with current `jti` and `parent_jti`. | Required before ClipTown can enforce full grant lineage. |
| 2 | `shared-auth/shared-auth-clients#34` | Official exact-audience Rust introspection client. | Used by ClipTown; establishes the reviewed transport contract. |
| 3 | `cliptown/cliptown-rust-backend.rs#8` | Production transfer routes, authorization, RLS/persistence, idempotency, readiness, headless E2E. | Required ClipTown API implementation. |
| 4 | `memebank/mbk-rest-api#7` | Compose official shared-auth delegation and ClipTown Go SDKs in the active MemeBank backend. | MemeBank-owned activation item. |
| 5 | `cliptown-test/memebank-image-interop#7` and MemeBank test evidence | Prove no-phone-app API interoperability and failure behavior. | Must be green against immutable source/release versions. |

The earlier boundary work is merged in `memebank/mbk-rest-api#6`; DEN-2259 completes production composition, pinning, configuration, and evidence.

## Required MemeBank composition

For each operation, MemeBank must:

1. accept the normal shared-auth user session at the product boundary;
2. ask the official shared-auth SDK for exactly one ClipTown delegated scope;
3. validate the returned token type, audience, exact scope, bounded lifetime, and expiry before use;
4. pass the delegated bearer only to the official ClipTown SDK token provider;
5. call the corresponding versioned SDK method;
6. map errors without logging or returning tokens, ciphertext, credentials, private URLs, or provider details.

Operation mapping:

- list/get → `cliptown:memebank:read`
- create/acknowledge → `cliptown:memebank:write`
- cancel → `cliptown:memebank:delete`

Write and delete assurance is enforced by shared-auth policy. MemeBank must not determine that a particular factor application was used; it consumes normalized assurance only.

## Data boundary

The ClipTown transfer envelope may contain ciphertext and bounded routing/integrity metadata. It must not contain access or refresh tokens, the introspection service credential, OTP seeds/codes, biometric material, private keys, provider credentials, durable private object URLs, signed upload/download URLs, plaintext OCR, captions, tags, or image bytes in metadata fields.

MemeBank retains ownership of source assets and sharing policy. ClipTown authorizes every transfer against the delegated subject; a service credential is never a cross-tenant bypass.

## Acceptance evidence

MemeBank qualification must include:

- Go formatting, vet, race tests, and the repository security gates;
- dependency/source checks proving no direct 3FA package or endpoint;
- source checks proving no raw ClipTown HTTP route duplication outside the official SDK;
- exact read/write/delete delegation requests;
- invalid idempotency keys and transfer identifiers failing before delegation/network work;
- wrong audience, broadened/missing scope, malformed bearer type, expiry, and excessive TTL failing closed;
- ClipTown outage returning a controlled unavailable result with no local-app or clipboard fallback;
- a headless end-to-end flow with neither mobile app installed.

## GitHub Project mapping

Add each active item to the MemeBank organization project using:

- **Linear**: `DEN-2259`
- **Workstream**: `Shared auth and ClipTown`
- **Status**: In progress / In review / Qualified / Merged / Released / Deployed
- **Owner**: service or SDK owner
- **Environment**: none / test / staging / production
- **Dependency version**: immutable commit, package version, or release digest
- **Evidence**: exact green workflow or canary record
- **Blocked by**: URL of the upstream item

Do not mark the MemeBank item Qualified until official SDK composition is present in the active service and the no-phone-app flow is green. Do not mark it Deployed until delegation policy, endpoint configuration, credentials, observability, and rollback are verified in the target environment.

## Rollout and rollback

Roll out in non-production with narrow delegation policy, exact ClipTown endpoint configuration, one service replica, bounded traffic, and metadata-only telemetry. Expand only after authorization, idempotency, ownership, latency, and outage behavior are observed.

Rollback by reverting the MemeBank service version and disabling or narrowing its ClipTown delegation policy. Never roll back by accepting direct 3FA artifacts, reusing a broad bearer, sharing credentials, bypassing the official SDK, or using a mutually installed mobile application as the integration bridge.
