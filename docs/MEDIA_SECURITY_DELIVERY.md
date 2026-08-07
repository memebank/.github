# MemeBank media-security delivery

This document is the organization-level execution plan for server-managed media encryption, asynchronous image analysis, client-vault behavior, exact-version object access, and plaintext-lifecycle controls.

## Planning and execution systems

- **GitHub organization:** `memebank`
- **GitHub Project:** `memebank-project` — project 1
- **Linear project:** `memebank`
- **Primary Linear issue:** `DEN-1535`
- **Primary implementation repository:** `memebank/mbk-ocr-api`
- **Latest merged delivery PR:** `memebank/mbk-ocr-api#21`
- **Current implementation issue:** `memebank/mbk-ocr-api#23`
- **Current verification issue:** `memebank/mbk-ocr-api#24`
- **Current delivery PR:** `memebank/mbk-ocr-api#21`

GitHub is authoritative for commits, pull requests, reviews, Actions evidence, releases, and deployable artifacts. Linear is authoritative for priority, ownership, milestones, dependencies, product status, and decision documents. The GitHub Project provides the organization-level execution board; the durable routing card is `.github#2`.

## Product decision

MemeBank’s normal analyzable media mode is:

```text
transport: TLS
storage: private object storage
at rest: server-managed SSE-KMS
analysis: asynchronous enabled
plaintext disk: forbidden
```

An optional future client-vault mode encrypts on the device before upload. Client-vault objects remain opaque to MemeBank and cannot enter server OCR, thumbnail, caption, embedding, moderation, perceptual-hash, or re-indexing pipelines.

## Merged security boundaries

The live Go compatibility service now includes executable contracts for:

1. client-vault and analysis-disabled rejection before object access;
2. bounded in-memory plaintext streams with deterministic closure;
3. exact immutable object-version/generation references;
4. required SSE-KMS, approved full KMS key ARNs, and S3 Bucket Keys;
5. object-bound leases and monotonically increasing fencing tokens;
6. heartbeat renewal, hard expiry, cancellation, and stale-worker suppression;
7. durable PostgreSQL acquisition, renewal, private staging, and atomic result publication;
8. fenced cleanup of abandoned private result versions;
9. exact-version S3 result deletion and scheduled cleanup runtime;
10. one-owner transactional reference semantics under concurrency;
11. tenant/library/asset/job/worker authorization before storage;
12. provider-neutral exact-version reads with no `latest` fallback;
13. concrete AWS SDK v2 exact-version S3 reads with expected-owner pinning.

## Latest merged delivery: exact-version S3 reads

PR `memebank/mbk-ocr-api#21` was squash-merged as:

```text
a0d8a2d8ef023f92b60565db7581ba33e572b133
```

Every AWS read contains:
12. provider-neutral exact-version reads with no `latest` fallback.

## Latest merged delivery: exact-version S3 reads

PR `memebank/mbk-ocr-api#21` was squash-merged as:

```text
a0d8a2d8ef023f92b60565db7581ba33e572b133
```

Every AWS read contains:

```text
Bucket
Key
VersionId
ExpectedBucketOwner
```

The reader is bound to one approved private bucket, one opaque key prefix, and one AWS account owner. It rejects cross-bucket, sibling-prefix, prefix-only, unsafe-key, missing-version, and S3 `null`-version requests before AWS.

It requires response `VersionId` to equal the queued durable version and returns content length, media type, SSE mode, KMS key identity, and Bucket Key state from the same response body. The existing stream policy then enforces byte, media, KMS, and Bucket-Key constraints.

The implementation includes mocked SDK tests, signed wire-level SDK tests, an isolated pinned Go module, a dedicated Actions workflow, and deployment/IAM guidance.

## Merge evidence

The first focused workflow run exposed an isolated harness omission: its temporary module lacked the existing identifier-policy dependency. Adding the whole PostgreSQL store then exposed duplicate helper coupling. The adapter was refactored to own a narrow S3 identifier validator, and the unnecessary database dependency was removed. The security behavior remained fail-closed.

The exact merged head passed all eight workflows:

```text
s3-versioned-read-security
analysis-authorized-versioned-source
analysis-transaction-store
analysis-stream-security
s3-result-cleanup-security
s3-cleanup-runtime-security
workflow-hygiene-security
ci
```

The tested head was marked ready only after all checks passed, and the merge used that exact head SHA.

## Current production milestones

### Issue #23 — shared-auth and workload identity
It requires response `VersionId` to equal the queued durable version and returns content length, media type, SSE mode, KMS key identity, and Bucket Key state from the same response body. The existing stream policy then enforces byte/media/KMS limits.

## Merge evidence

The first focused workflow run exposed an isolated harness omission: its temporary module lacked the existing identifier-policy dependency. Adding the whole PostgreSQL store then exposed duplicate helper coupling. The adapter was refactored to own a narrow S3 identifier validator, and the unnecessary database dependency was removed. The security behavior remained fail-closed.

The exact merged head passed all eight workflows:

```text
s3-versioned-read-security
analysis-authorized-versioned-source
analysis-transaction-store
analysis-stream-security
s3-result-cleanup-security
s3-cleanup-runtime-security
workflow-hygiene-security
ci
```

The tested head was marked ready only after all checks passed, and the merge used that exact head SHA.

## Current production milestones

### Issue #23 — shared-auth and workload identity

- implement a durable service-principal authorizer;
- compare queue/request identifiers against the canonical job record;
- enforce tenant, library, asset, region, residency, retention, and legal-hold policy;
- emit opaque security audit events without media, keys, provider messages, or credentials;
- wire authorization into every OCR and enrichment handler;
- add cross-tenant E2E using the shared-auth test environment.

### Issue #24 — provider conformance and plaintext proof

- deploy least-privilege `s3:GetObjectVersion` and `kms:Decrypt` policy;
- add LocalStack or AWS test-account failure injection for permissions, throttling, deleted versions, delete markers, KMS denial, mid-stream disconnects, and cancellation;
- monitor worker filesystems through success, rejection, cancellation, timeout, crash, panic, restart, and termination;
- prove no persistent plaintext or derived-content artifact remains;
- run evidence in GitHub Actions and the internal GHA-compatible worker path.

### Additional platform work

- implement an R2 or provider-equivalent immutable-generation reader;
- prove missing versions never fall back to mutable current objects;
- port storage, authorization, lease, heartbeat, result-transaction, and cleanup contracts to Rust;
- integrate with SeaORM/SQLx and async `AsyncRead` pipelines;
- sandbox decoders and model subprocesses.
- emit opaque security audit events without media, keys, provider messages, or credentials.

### Issue #24 — provider conformance and plaintext proof

- deploy least-privilege `s3:GetObjectVersion` and `kms:Decrypt` policy;
- add LocalStack or AWS test-account failure injection for permissions, throttling, deleted versions, delete markers, KMS denial, mid-stream disconnects, and cancellation;
- monitor worker filesystems through success, rejection, cancellation, timeout, crash, panic, restart, and termination;
- prove no persistent plaintext or derived-content artifact remains;
- run evidence in GitHub Actions and the internal GHA-compatible worker path.

### Additional platform work

- implement an R2 or provider-equivalent immutable-generation reader;
- prove missing versions never fall back to mutable current objects;
- port storage, authorization, lease, heartbeat, result-transaction, and cleanup contracts to Rust;
- integrate with SeaORM/SQLx and async `AsyncRead` pipelines;
- sandbox decoders and model subprocesses.

## Repository ownership

- `mbk-ocr-api`: image input, provider, worker, lease, result-publication, cleanup, and compatibility security contracts.
- `mbk-rest-api` / `mbk-api`: upload planning, asset policy, customer API authorization, and visible-result delivery.
- `mbk-pwa`: user-facing server-managed versus client-vault UX and capability explanations.
- `mbk-scripts`: migration, audit, repair, and controlled operational tooling.
- `.github`: organization routing, governance, project documentation, and cross-repository delivery evidence.

## Status update policy

Every substantial increment should update all three layers:

1. GitHub PR with exact code, tests, and Actions evidence;
2. Linear issue/project document with product status and remaining dependencies;
3. organization GitHub Project routing card and this delivery document with current PR/issue links.

Do not mark `DEN-1535` complete until real shared-auth authorization, concrete production provider clients, handler wiring, canonical Rust integration, cross-tenant/provider E2E, and no-persistent-plaintext proof are all complete.