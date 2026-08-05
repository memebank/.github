#!/usr/bin/env python3
"""Validate MemeBank organization project and repository delivery metadata."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RELATIONSHIPS = ROOT / "repository-relationships.json"
PROJECT_CONTEXT = ROOT / "project-context.yaml"
PROJECTS_DOC = ROOT / "docs/PROJECTS.md"
FLEET_DOC = ROOT / "docs/REPOSITORY_FLEET.md"
VISION_DOC = ROOT / "docs/VISION_OCR_DELIVERY.md"
PROFILE = ROOT / "profile/README.md"

OBSERVED = (
    ".github",
    "mbk-api",
    "mbk-ocr-api",
    "mbk-pwa",
    "mbk-rest-api",
    "mbk-scripts",
    "memebanc-blog",
    "stop-billing",
)

CANONICAL = (
    ".github",
    "mb-interfaces",
    "mb-clients",
    "mb-cli",
    "memebank-api-server.rs",
    "memebank-web-server.rs",
    "memebank-media-worker.rs",
    "memebank-flutter",
    "mb-infra",
    "memebank.github.io",
    "memebank-mcp-server.rs",
    "memebank-e2e",
    "memebank-monorepo",
)

GITHUB_PROJECT_URL = "https://github.com/orgs/memebank/projects/1"
LINEAR_PROJECT_URL = "https://linear.app/denman/project/memebank-3db5f5cc7452"
FORBIDDEN_CREDENTIAL = re.compile(
    r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|BEGIN [A-Z ]*PRIVATE KEY)"
)


class ContractError(ValueError):
    pass


def fail(message: str) -> None:
    raise ContractError(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot parse {path.relative_to(ROOT)}: {error}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def require_unique_names(records: Any, label: str) -> list[dict[str, Any]]:
    if not isinstance(records, list):
        fail(f"{label} must be an array")
    normalized: list[dict[str, Any]] = []
    names: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            fail(f"{label}[{index}] must be an object")
        name = record.get("name")
        if not isinstance(name, str) or not name:
            fail(f"{label}[{index}].name must be nonempty")
        names.append(name)
        normalized.append(record)
    if len(names) != len(set(names)):
        fail(f"{label} contains duplicate repository names")
    return normalized


def validate_relationships() -> None:
    document = load_json(RELATIONSHIPS)
    if document.get("schema_version") != 2:
        fail("repository-relationships schema_version must equal 2")
    if document.get("organization") != "memebank":
        fail("repository-relationships organization must equal memebank")
    if document.get("observed_at") != "2026-08-05":
        fail("repository-relationships observed_at changed unexpectedly")

    planning = document.get("planning")
    if not isinstance(planning, dict):
        fail("planning must be an object")
    if planning.get("github_project_number") != 1:
        fail("canonical GitHub Project number must equal 1")
    if planning.get("github_project_url") != GITHUB_PROJECT_URL:
        fail("canonical GitHub Project URL changed")
    if planning.get("linear_project_url") != LINEAR_PROJECT_URL:
        fail("canonical Linear project URL changed")

    observed = require_unique_names(document.get("observed_repositories"), "observed_repositories")
    observed_names = tuple(record["name"] for record in observed)
    if observed_names != OBSERVED:
        fail(f"observed repository inventory changed: {observed_names!r}")
    for record in observed:
        if record.get("visibility") not in {"public", "private"}:
            fail(f"invalid visibility for observed repository {record['name']}")
        if not isinstance(record.get("default_branch"), str) or not record["default_branch"]:
            fail(f"missing default branch for observed repository {record['name']}")
    if observed[0].get("visibility") != "public" or observed[0].get("default_branch") != "main":
        fail(".github must remain the public main-branch organization profile")
    if any(record.get("visibility") != "private" for record in observed[1:]):
        fail("all observed legacy repositories must remain recorded as private")

    canonical = require_unique_names(document.get("canonical_targets"), "canonical_targets")
    canonical_names = tuple(record["name"] for record in canonical)
    if canonical_names != CANONICAL:
        fail(f"canonical target order changed: {canonical_names!r}")
    if canonical[0].get("state") != "observed" or canonical[0].get("visibility") != "public":
        fail("canonical .github target must reflect the observed public profile repository")
    for record in canonical[1:]:
        if record.get("state") != "planned" or record.get("visibility") != "private":
            fail(f"planned canonical target {record['name']} must remain private and planned")

    migration = document.get("migration_policy")
    if not isinstance(migration, dict):
        fail("migration_policy must be an object")
    if migration.get("canonical_infrastructure_repository") != "mb-infra":
        fail("mb-infra must remain the canonical infrastructure repository")
    if migration.get("forbidden_repository_names") != ["memebank-infra"]:
        fail("forbidden repository-name policy changed")
    if migration.get("legacy_repositories_are_preserved") is not True:
        fail("legacy repository preservation must remain enabled")
    if migration.get("silent_history_deletion_forbidden") is not True:
        fail("silent history deletion must remain forbidden")
    if migration.get("monorepo_published_last") is not True:
        fail("monorepo publication ordering changed")


def validate_text_contracts() -> None:
    texts = {
        "project-context.yaml": PROJECT_CONTEXT.read_text(encoding="utf-8"),
        "docs/PROJECTS.md": PROJECTS_DOC.read_text(encoding="utf-8"),
        "docs/REPOSITORY_FLEET.md": FLEET_DOC.read_text(encoding="utf-8"),
        "docs/VISION_OCR_DELIVERY.md": VISION_DOC.read_text(encoding="utf-8"),
        "profile/README.md": PROFILE.read_text(encoding="utf-8"),
    }
    combined = "\n".join(texts.values())

    required = (
        GITHUB_PROJECT_URL,
        LINEAR_PROJECT_URL,
        "semantic",
        "DEN-1005",
        "DEN-1011",
        "DEN-1018",
        "mb-infra",
        "memebank-media-worker.rs",
        "memebank-monorepo",
        "production dependency",
        "ImagePreprocessor",
        "OcrProvider",
        "EmbeddingProvider",
        "gross",
    )
    # "gross" is not an OCR concept and is intentionally not required here.
    required = tuple(value for value in required if value != "gross")
    for token in required:
        if token not in combined:
            fail(f"organization delivery documentation is missing {token!r}")

    if "memebank-infra" not in texts["docs/REPOSITORY_FLEET.md"]:
        fail("fleet documentation must explicitly reject the superseded infrastructure name")
    if "all of `ours`" not in texts["docs/PROJECTS.md"]:
        fail("project documentation must preserve the semantic merge policy")
    if "face recognition" not in texts["docs/VISION_OCR_DELIVERY.md"]:
        fail("vision documentation must preserve the biometric MVP exclusion")

    for path, text in texts.items():
        if FORBIDDEN_CREDENTIAL.search(text):
            fail(f"credential-shaped content detected in {path}")
        if re.search(r"(?m)^(<<<<<<<|=======|>>>>>>>)", text):
            fail(f"merge conflict marker detected in {path}")


def main() -> int:
    try:
        validate_relationships()
        validate_text_contracts()
    except ContractError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "PASS MemeBank organization delivery contract: "
        f"observed={len(OBSERVED)} canonical={len(CANONICAL)} project=1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
