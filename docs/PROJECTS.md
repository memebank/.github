<!-- org-project-routing:start -->
# Project routing

- **GitHub organization:** [memebank](https://github.com/memebank)
- **Canonical GitHub Project:** [memebank-project](https://github.com/orgs/memebank/projects/1) (project 1)
- **Canonical Linear project:** [planning workspace](https://linear.app/denman/project/memebank-3db5f5cc7452)
- **Organization documentation repository:** [memebank/.github](https://github.com/memebank/.github)

## Source-of-truth boundaries

GitHub is authoritative for repositories, commits, pull requests, reviews, CI checks, releases, deployable artifacts, and runtime evidence. Linear is authoritative for product planning, priorities, ownership, dependencies, milestones, and status reporting. The GitHub Project is the organization-level execution board and should contain the governance issue maintained by this repository.

## Change and merge policy

Documentation branches must be reviewed through pull requests and merged after checks pass. Concurrent edits are reconciled semantically against the latest default branch: this managed routing block is regenerated while all unrelated prose outside the block is preserved. Do not resolve conflicts by blindly choosing one side.

A semantic merge reconstructs the compatible intent of both sides; never resolve a substantive conflict by selecting all of `ours` or all of `theirs`.
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