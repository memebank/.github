# `memebank` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **1**
- Private repository names withheld: **37**
- Relationship edges: **4**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/memebank/.github) | `organization_governance` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `organization://memebank` | `coordinates_via` | `capability://fiducia-cloud/distributed-coordination` | `platform-default` / `explicit-platform-decision`: locks, leases, idempotency, elections, schedules, budgets, and task claims |
| `organization://memebank` | `authenticates_via` | `capability://shared-auth/human-identity` | `platform-default` / `explicit-platform-decision`: platform human identity and session authority |
| `organization://memebank` | `uses_capability` | `organization://3FA-app` | `declared` / `explicit-product-decision`: step-up authentication |
| `organization://memebank` | `interoperates_with` | `organization://cliptown` | `declared` / `explicit-product-decision`: API/SDK clipboard and media exchange |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
