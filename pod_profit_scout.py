#!/usr/bin/env python3
"""POD Profit Scout: simple product readiness checker.

Usage:
    python pod_profit_scout.py sample_catalog.json
"""

from __future__ import annotations

import json
import sys
from datetime import UTC, datetime
from pathlib import Path

REQUIRED_FIELDS = ["sku", "title", "price", "tags", "image", "mockup"]


def load_catalog(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "products" in data:
        data = data["products"]
    if not isinstance(data, list):
        raise ValueError("Catalog must be a list or an object with a products list.")
    return data


def check_product(product: dict, base_dir: Path) -> dict:
    missing_fields = [field for field in REQUIRED_FIELDS if not product.get(field)]
    missing_files = []
    for field in ["image", "mockup"]:
        value = product.get(field)
        if value and not (base_dir / value).exists():
            missing_files.append(value)
    ready = not missing_fields and not missing_files
    return {
        "sku": product.get("sku", "UNKNOWN"),
        "title": product.get("title", "Untitled"),
        "ready": ready,
        "missing_fields": missing_fields,
        "missing_files": missing_files,
        "price": product.get("price", ""),
        "tags": product.get("tags", []),
    }


def write_report(results: list[dict], output: Path) -> None:
    ready_count = sum(1 for item in results if item["ready"])
    blocked_count = len(results) - ready_count
    lines = [
        "# POD Readiness Report",
        "",
        f"Generated: {datetime.now(UTC).isoformat(timespec='seconds')}",
        "",
        f"Products checked: {len(results)}",
        f"Ready products: {ready_count}",
        f"Blocked products: {blocked_count}",
        "",
        "## Product status",
        "",
    ]
    for item in results:
        status = "READY" if item["ready"] else "BLOCKED"
        lines.append(f"### {status}: {item['sku']} — {item['title']}")
        lines.append(f"- Price: {item['price']}")
        lines.append(f"- Tags: {', '.join(map(str, item['tags'])) if item['tags'] else 'none'}")
        if item["missing_fields"]:
            lines.append(f"- Missing fields: {', '.join(item['missing_fields'])}")
        if item["missing_files"]:
            lines.append(f"- Missing files: {', '.join(item['missing_files'])}")
        if item["ready"]:
            lines.append("- Next action: publish or queue for listing.")
        else:
            lines.append("- Next action: fix blockers before listing.")
        lines.append("")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python pod_profit_scout.py <catalog.json>", file=sys.stderr)
        return 2
    catalog_path = Path(sys.argv[1])
    products = load_catalog(catalog_path)
    results = [check_product(product, catalog_path.parent) for product in products]
    output = Path("reports") / "pod_readiness_report.md"
    write_report(results, output)
    ready_count = sum(1 for item in results if item["ready"])
    print(f"checked={len(results)} ready={ready_count} blocked={len(results) - ready_count} report={output}")
    return 0 if ready_count == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
