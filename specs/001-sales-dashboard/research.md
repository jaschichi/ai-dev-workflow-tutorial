# Research: Sales Dashboard

**Date**: 2026-04-19 | **Branch**: `001-sales-dashboard`

## Decision 1: Data Generation Strategy

**Decision**: NumPy seeded random generation via `numpy.random.default_rng(seed=42)`

**Rationale**: NumPy ships as a transitive dependency of Pandas — no new package needed.
`default_rng` is the modern NumPy API (preferred over `numpy.random.seed` which mutates
global state). Seed 42 produces reproducible data across all deployments and environments.

**Alternatives considered**:
- Faker: realistic names but adds a dependency (violates Principle III)
- Pure Python `random`: viable but NumPy vectorized ops are faster for 1,000-row generation
- CSV file: violates Principle II (no file-based data sources)

---

## Decision 2: Code Structure

**Decision**: Three flat files at repo root — `data.py`, `charts.py`, `app.py`

**Rationale**: Streamlit Community Cloud requires `app.py` at root. Three-file split cleanly
separates concerns (generation / rendering / wiring) while staying readable for a portfolio
viewer skimming the source. No package init or imports from nested modules needed.

**Alternatives considered**:
- Single `app.py`: simple but mixes concerns, harder to show modular thinking to portfolio reviewers
- `src/` package layout: over-engineered for < 300 total lines; breaks Community Cloud defaults

---

## Decision 3: Sales Trend Granularity

**Decision**: Monthly aggregation — 12 data points (Jan–Dec)

**Rationale**: 12 points fit cleanly on a line chart without crowding x-axis labels. Monthly
view matches executive reporting cadence (as described in PRD user stories). Daily (365 points)
would appear noisy without smoothing; weekly (52 points) splits the difference but gains little.

**Alternatives considered**:
- Daily: too noisy for a portfolio dashboard targeting general public
- Weekly: moderate improvement but adds complexity for marginal gain

---

## Decision 4: Color Theme

**Decision**: Streamlit dark theme (`theme.base = "dark"`) with Plotly `plotly_dark` template

**Rationale**: Dark-themed dashboards read as more sophisticated/professional to a general
public audience. Consistent use of `plotly_dark` template across all three charts ensures
visual coherence without per-chart color overrides.

**Implementation notes**:
- Set via `.streamlit/config.toml`: `[theme] base = "dark"`
- Pass `template="plotly_dark"` to every `go.Figure` or `px.*` call in `charts.py`
- KPI metric cards inherit Streamlit's dark theme automatically via `st.metric`

**Alternatives considered**:
- Default Streamlit blue/gray: safe but unremarkable for portfolio
- Custom brand palette: adds per-chart color mapping complexity with no structural benefit
- Monochromatic: less visually distinct between chart series

---

## Decision 5: Synthetic Data Schema

**Decision**: Generate a DataFrame with columns matching PRD data spec, using seeded NumPy

| Column | Type | Generation |
|--------|------|------------|
| date | datetime | 365 daily dates across 2024, sampled randomly |
| order_id | str | `ORD-{n:06d}` sequential |
| product | str | Random choice from 15 product names |
| category | str | Random choice from 5 categories (weighted) |
| region | str | Random choice from 4 regions (uniform) |
| quantity | int | randint(1, 5) |
| unit_price | float | Choice from price table per category |
| total_amount | float | quantity × unit_price |

Target output: ~1,000 rows, reproducible with `seed=42`.
