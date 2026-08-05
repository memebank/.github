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

Documentation and implementation branches are reviewed through pull requests. Concurrent edits are reconciled semantically against the latest default branch: preserve compatible product behavior, contracts, migrations, tests, security controls, observability, documentation, and rollback paths; reject obsolete topology, duplicated authority, temporary credentials, silent capability collapse, or weakened validation.

Do not resolve substantive conflicts by blindly choosing all of `ours`, all of `theirs`, current, or incoming. Record the conceptual decision in the pull request and the relevant Linear issue.
<!-- org-project-routing:end -->
