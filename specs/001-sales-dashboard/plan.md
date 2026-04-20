# Implementation Plan: Sales Dashboard

**Branch**: `001-sales-dashboard` | **Date**: 2026-04-19 | **Spec**: `specs/001-sales-dashboard/spec.md`
**Input**: Feature specification from `prd/ecommerce-analytics.md` + constitution v1.0.0

## Summary

Build a portfolio-ready Streamlit sales analytics dashboard that generates synthetic e-commerce
data at runtime (seeded NumPy), displays two KPI scorecards, and renders three Plotly charts
(monthly sales trend, category breakdown, regional breakdown) with a dark theme throughout.

## Technical Context

**Language/Version**: Python 3.9+ (Streamlit Community Cloud compatible)
**Primary Dependencies**: Streamlit, Pandas, Plotly, NumPy (Pandas transitive dep)
**Storage**: N/A — all data generated at runtime; no persistence layer
**Testing**: Manual visual QA; no automated test suite required for v1
**Target Platform**: Web browser (Chrome, Firefox, Safari, Edge) via Streamlit Community Cloud
**Project Type**: Single-page web application
**Performance Goals**: Dashboard loads within 5 seconds; charts render within 2 seconds
**Constraints**: No external databases, no CSV files, no auth; Plotly + Streamlit dark theme
**Scale/Scope**: Single user per session; ~1,000 synthetic transaction rows per load

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Visual Polish | ✅ PASS | Dark theme + Plotly; all charts styled consistently |
| II. Simulated Data | ✅ PASS | NumPy seeded generation; no CSV or DB |
| III. Minimal Dependencies | ✅ PASS | Streamlit, Pandas, Plotly, NumPy only |
| IV. Iterative Increments | ✅ PASS | P1 KPIs → P2 trend chart → P3 bar charts |
| V. Portfolio Readiness | ✅ PASS | Dark theme, no debug output, clean layout |

**All gates pass. Proceeding to Phase 0.**

## Project Structure

### Documentation (this feature)

```text
specs/001-sales-dashboard/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit-tasks)
```

### Source Code (repository root)

```text
app.py          # Streamlit entry point — layout, page config, dark theme, wiring
data.py         # Synthetic data generation — seeded NumPy, returns DataFrames
charts.py       # Plotly figure builders — one function per chart type
requirements.txt
```

**Structure Decision**: Flat three-file layout at repo root. No `src/` nesting — Streamlit Community
Cloud expects `app.py` at the root, and the small scope (< 300 lines total) does not justify
deeper hierarchy.

## Complexity Tracking

> No constitution violations — this section is intentionally empty.
