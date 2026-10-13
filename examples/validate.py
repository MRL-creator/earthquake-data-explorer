"""Compare application summaries with an independent standard-library CSV calculation."""

from collections import Counter
import csv
from pathlib import Path
from statistics import mean
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from earthquake_explorer.analysis import EventFilters, calculate_summary, filter_events
from earthquake_explorer.analysis.statistics import count_over_time, magnitude_histogram
from earthquake_explorer.data import load_csv


def validate():
    path = ROOT / "sample_data" / "usgs_2025_q1_m5plus.csv"
    with path.open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source))
    loaded = load_csv(path)
    summary = calculate_summary(loaded.events)
    magnitudes = [float(row["magnitude"]) for row in rows]
    depths = [float(row["depth_km"]) for row in rows]
    expected_months = dict(sorted(Counter(row["time"][:7] for row in rows).items()))
    monthly = count_over_time(loaded.events, "MS")
    actual_months = dict(zip(monthly.period_start.dt.strftime("%Y-%m"), monthly.event_count))
    selected = filter_events(loaded.events, EventFilters(magnitude_range=(6.0, 10.0)))
    expected_ids = {row["event_id"] for row in rows if float(row["magnitude"]) >= 6.0}
    checks = {
        "snapshot event count": len(rows) == summary.event_count == 396,
        "no skipped records": loaded.skipped_rows == 0,
        "largest reported magnitude": max(magnitudes) == summary.largest_magnitude == 7.7,
        "mean reported magnitude": abs(mean(magnitudes) - summary.mean_magnitude) < 1e-9,
        "mean reported depth": abs(mean(depths) - summary.mean_depth_km) < 1e-9,
        "deep event count": sum(depth > 300 for depth in depths) == summary.deep_count == 13,
        "monthly counts": actual_months == expected_months,
        "histogram conservation": int(magnitude_histogram(loaded.events).event_count.sum()) == 396,
        "M >= 6 selection": {event.event_id for event in selected} == expected_ids and len(selected) == 22,
    }
    for label, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'} / {label}")
    print(f"Monthly counts: {expected_months}")
    print(f"Mean reported magnitude: {summary.mean_magnitude:.6f}")
    print(f"Mean depth: {summary.mean_depth_km:.6f} km")
    if not all(checks.values()):
        raise AssertionError("Catalog validation failed: " + ", ".join(label for label, ok in checks.items() if not ok))


if __name__ == "__main__":
    validate()
