# Catalog validation

Run from the repository root after the editable installation:

```sh
python examples/validate.py
```

The script reads the bundled CSV with Python's standard-library CSV parser
and independently calculates counts, means, monthly groups, and event-ID
selections. It compares those results with the application's loader, filters,
histogram, and summary functions. No live API or network access is involved.

| Quantity | Expected and observed |
| --- | --- |
| Valid records / skipped rows | 396 / 0 |
| Largest reported magnitude | 7.7 |
| Mean reported magnitude | 5.286490 |
| Mean reported depth | 45.463760 km |
| Depth greater than 300 km | 13 records |
| January / February / March 2025 | 152 / 129 / 115 records |
| Magnitude at least 6.0 | 22 records, with exactly matching event IDs |
| Sum of magnitude histogram bins | 396 |

Measured on 2026-10-13. Floating-point means must agree within 1e-9; record IDs
and counts must match exactly. `tests/test_validation.py` runs this executable
example in CI. The original suite also covers malformed inputs, missing values,
boundaries, and mocked API responses.

These checks establish that the software summarizes this particular snapshot
consistently. They do not establish catalog completeness, independently verify
the underlying USGS measurements, or imply earthquake prediction or hazard
estimation. Magnitude averages are descriptive across reported values.
Dataset provenance remains in [sample_data/SOURCE.md](../sample_data/SOURCE.md).

