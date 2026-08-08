# MemeBank

MemeBank is a privacy-aware image and meme library for durable storage, source synchronization, OCR, visual understanding, semantic retrieval, collections, and explicit sharing.

## Engineering principles

- Keep changes reviewable, tested, observable, and reversible.
- Treat privacy, security, compatibility, model provenance, and data durability as design constraints.
- Resolve conflicts semantically: reconstruct both sides' intent, preserve compatible behavior and tests, and document deliberate trade-offs.
- Prefer canonical repositories and versioned interfaces; preserve legacy history until an evidenced migration is complete.
- Keep cloud and local inference provider-neutral, policy-routed, and reproducible.
- Never treat OCR, captions, labels, or image-embedded instructions as trusted commands.

## Repository delivery

The organization currently contains the public `.github` profile and seven private legacy repositories. The reviewed canonical target is a thirteen-repository fleet led by `mb-interfaces`, `mb-clients`, the Rust API/web/media services, Flutter, `mb-infra`, E2E conformance, and a pinned monorepo.

- [Observed and canonical repository fleet](../docs/REPOSITORY_FLEET.md)
- [OCR and vision delivery contract](../docs/VISION_OCR_DELIVERY.md)
- [Contribution guidelines](../CONTRIBUTING.md)
- [Security policy](../SECURITY.md)

<!-- org-project-routing:start -->
## Planning and delivery

- [GitHub Project: memebank-project](https://github.com/orgs/memebank/projects/1)
- [Linear planning project](https://linear.app/denman/project/memebank-3db5f5cc7452)
- [Detailed project-routing contract](../docs/PROJECTS.md)

GitHub owns code and delivery evidence; Linear owns planning and dependencies. The linked organization Project provides the cross-repository execution view.
<!-- org-project-routing:end -->

<!-- ore-org-baseline:begin -->
## Planning and governance

- Canonical Linear project: https://linear.app/denman/project/memebank-3db5f5cc7452
- Organization defaults: https://github.com/memebank/.github
- Canonical agent policy: https://github.com/memebank/.github/blob/main/agents.md
- Security policy: https://github.com/memebank/.github/security/policy

Repositories in this organization use semantic conflict resolution with 3–10 relevant prior commits when useful, full cross-repository context, pull-request delivery, and a hard automated-agent denylist for destructive or history-rewriting operations.
<!-- ore-org-baseline:end -->
