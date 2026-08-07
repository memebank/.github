# MemeBank canonical fleet publication

- Repository: `memebank/.github`
- Repository URL: https://github.com/memebank/.github
- Role: `Organization profile, shared policies, and reusable GitHub configuration`
- Visibility: `public organization-profile exception`
- Approved source tree: `6f885dadcfcd4192c7c10e64beccd91ea695bbd7`
- Approved source head: `389f9ac5ecc056dab7e3b6b426568ccefe1a6876`
- Source archive SHA-256: `b451cce7de72ce67ad7dd135db794d54f34ff6b83c2d5bf8a7c0baf6df91b167`
- GitHub Project: [memebank-project](https://github.com/orgs/memebank/projects/1)
- Linear tracking: `DEN-1004, DEN-1005, DEN-1043, DEN-319, DEN-1011, DEN-1018`

## Authority and migration boundary

The sealed source-v2 carrier is maintained in `ORESoftware/ai-agent-coordinator.rs`.
The approved source commit was published without force-pushing or rewriting legacy
MemeBank repositories. Legacy `mbk-*`, `Memebank`, `playground`, and migration
repositories remain separate until a focused migration PR explicitly supersedes them.

`memebank/.github` is an additive semantic merge exception: its newer public
organization governance is preserved rather than replaced by the sealed source
snapshot. All other canonical repositories are private by default.

## Change policy

Resolve conflicts semantically using the merge base, relevant history, contracts,
tests, security controls, observability, and rollback intent. Never resolve a
substantive conflict by selecting an entire side wholesale.
