<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [memebank](https://github.com/memebank)
- **Canonical GitHub Project:** [memebank-project](https://github.com/orgs/memebank/projects/1) (project 1)
- **Canonical Linear project:** [MemeBank](https://linear.app/denman/project/memebank-3db5f5cc7452)
- **Organization documentation repository:** [memebank/.github](https://github.com/memebank/.github)

## Source-of-truth boundaries

GitHub is authoritative for repositories, repository IDs, branches, commits, pull requests, reviews, checks, releases, deployable artifacts, rulesets, and runtime evidence. Linear is authoritative for product intent, priority, ownership, dependencies, milestones, acceptance criteria, and cross-organization planning. The GitHub Project is the organization-level execution board and should contain the corresponding GitHub issues and pull requests.

A Linear specification is not an implementation claim. A local archive, source carrier, generated plan, or coordinator commit is not evidence that a target repository exists. Remote creation and governance require live GitHub identity, baseline PR, checks, merge SHA, and ruleset evidence.

## Delivery streams

| Stream | Linear | GitHub execution evidence |
|---|---|---|
| Product umbrella | DEN-1004 | organization issues, PRs, milestones, and releases |
| Canonical repository fleet | DEN-1005 | [fleet ledger](REPOSITORY_FLEET.md), repository-creation and baseline PR issues |
| Organization governance | DEN-1043 | `.github` policy PRs, rulesets, CODEOWNERS, workflow and secret controls |
| Authenticated publication | DEN-319 | short-lived publishing identity, exact remote SHA and audit evidence |
| OCR/vision benchmark | DEN-1011 | [candidate and benchmark contract](VISION_OCR_DELIVERY.md), benchmark PRs and reports |
| OCR/vision adapters | DEN-1018 | provider-neutral implementation and conformance PRs |

GitHub issues should include their Linear key in the title or body. Linear updates should link the exact repository, PR/issue number, head and merge SHA, relevant check runs, and any remaining activation boundary.

## Organization Project policy

Project 1 is the cross-repository delivery view. At minimum it should track:

- the canonical thirteen-repository publication and governance issue;
- OCR and vision benchmark delivery;
- provider-neutral adapter implementation;
- legacy-to-canonical migrations;
- security, CI, release, and deployment blockers that span repositories.

Items are closed only when their GitHub and Linear acceptance evidence agree. A merged prerequisite does not close a deployment or activation item.

## Change and merge policy

Documentation branches must be reviewed through pull requests and merged after checks pass. Concurrent edits are reconciled semantically against the latest default branch: this managed routing block is regenerated while all unrelated prose outside the block is preserved. Do not resolve conflicts by blindly choosing one side.

A semantic merge reconstructs the compatible intent of both sides; never resolve a substantive conflict by selecting all of `ours` or all of `theirs`.
Documentation and implementation branches are reviewed through pull requests. Concurrent edits are reconciled semantically against the latest default branch: preserve compatible product behavior, contracts, migrations, tests, security controls, observability, documentation, and rollback paths; reject obsolete topology, duplicated authority, temporary credentials, silent capability collapse, or weakened validation.

Do not resolve substantive conflicts by blindly choosing all of `ours`, all of `theirs`, current, or incoming. Record the conceptual decision in the pull request and the relevant Linear issue.
<!-- org-project-routing:end -->

## Active delivery workstream

### Media encryption and asynchronous analysis

- **Organization delivery plan:** [MEDIA_SECURITY_DELIVERY.md](./MEDIA_SECURITY_DELIVERY.md)
- **Primary Linear issue:** [DEN-1535](https://linear.app/denman/issue/DEN-1535/implement-no-plaintext-disk-analysis-streams-and-client-vault-fail)
- **Latest merged implementation:** [mbk-ocr-api#21](https://github.com/memebank/mbk-ocr-api/pull/21) — `a0d8a2d8ef023f92b60565db7581ba33e572b133`
- **Current execution issue:** [mbk-ocr-api#23](https://github.com/memebank/mbk-ocr-api/issues/23) — shared-auth workload identity and durable authorization
- **Verification issue:** [mbk-ocr-api#24](https://github.com/memebank/mbk-ocr-api/issues/24) — provider fault injection and no-persistent-plaintext proof
- **Current implementation PR:** [mbk-ocr-api#21](https://github.com/memebank/mbk-ocr-api/pull/21)
- **Durable GitHub Project routing card:** [.github#2](https://github.com/memebank/.github/issues/2)

The workstream keeps server-managed SSE-KMS media as the analyzable default, preserves optional opaque client-vault behavior, and requires authorization-before-storage, immutable object versions, bounded in-memory plaintext streams, fenced workers, atomic result publication, exact-version cleanup, provider conformance, and filesystem proof.

Update this section whenever the active GitHub issue or PR, primary Linear issue, milestone, or activation boundary changes.
Update this section whenever the active implementation PR, primary Linear issue, or milestone changes.
Update this section whenever the active GitHub issue or PR, primary Linear issue, milestone, or activation boundary changes.