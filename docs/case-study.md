# Earthquake Data Explorer: making catalog records inspectable

## Problem and implementation

A catalog CSV is difficult to explore spatially or compare across time windows.
This project connects a bounded-timeout USGS client, validated event records,
reusable filters and summaries, and an interactive Streamlit/Plotly dashboard.
The work includes CSV ingestion/export, missing-value handling, maps, selection,
and descriptive charts.

## Decision and trade-off

A dated USGS snapshot is bundled so the first useful workflow does not depend
on an API call. A local geographic outline avoids remote basemap requests.
This makes the demo reproducible, but the snapshot is not a live view of the
catalog and the statistics do not establish detection completeness.

## Evidence

The [public demo](https://mrl-earthquake-explorer.streamlit.app/) opens with
396 records. Filtering to reported magnitude at least 6.0 selects 22.
An [independent CSV calculation](validation.md) verifies record IDs, monthly
counts, means, histogram totals, and deep-event counts against the app.
Tests also exercise missing data, malformed inputs, and mocked API responses.

## Engineering lesson and next step

Source provenance and missing measurements are part of the result. A useful
extension would be a downloadable summary that preserves the query, timestamp,
and interpretation limits alongside every chart.

