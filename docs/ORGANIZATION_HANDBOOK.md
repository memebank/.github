# memebank organization handbook

> Shared operating defaults for repositories maintained under **memebank**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

memebank maintains media capture, cataloging, search, analysis, storage, and sharing software. This `.github` repository is the canonical home for shared policy, reusable templates, community health files, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported platforms and storage providers, development and test commands, authoritative metadata and API formats, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Media components should also document encryption boundaries, retention and deletion, object identity, deduplication, OCR/vision provenance, derived metadata, sync and conflict behavior, provider limits, rights and moderation boundaries, and degraded modes.

## Change workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, privacy and data impact, validation, compatibility, migration, and rollback.
4. Test large, corrupt, duplicate, unsupported, encrypted, offline, partial-upload, deletion, and provider-failure paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves auditability.

## Evidence, security, and documentation

Pull requests should include reproducible commands, licensed synthetic or sanitized media fixtures, expected and observed metadata, negative-path coverage, documentation updates, and CI or local-equivalent evidence. Never commit credentials, encryption keys, private media, production metadata, or sensitive logs. Follow `SECURITY.md` for private reporting. Keep storage and trust boundaries explicit, derived-data provenance documented, examples sanitized, and important privacy, rights, compatibility, and operational decisions recorded.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profiles, descriptions, topics, and READMEs are current.
- [ ] Community health files and reusable issue/PR guidance are present.
- [ ] Encryption, retention, deletion, provenance, rights, sync, and provider behavior is documented.
- [ ] Required checks cover representative media, storage failure, privacy, compatibility, and supply-chain risk.
- [ ] Stale repositories are archived or clearly marked.
- [ ] GitHub Project and Linear links resolve and reflect completed work.
