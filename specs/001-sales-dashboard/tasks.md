---
description: "Task list for Sales Dashboard implementation"
---

# Tasks: Sales Dashboard

**Input**: Design documents from `specs/001-sales-dashboard/`
**Prerequisites**: plan.md ✅, data-model.md ✅, research.md ✅, quickstart.md ✅

**Tests**: No automated tests — manual visual QA at each phase checkpoint (per plan.md).

**Organization**: Tasks grouped by user story. Each phase is independently demonstrable.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)
- Exact file paths included in every description

---

## Phase 1: Setup

**Purpose**: Create project scaffold and configuration before any code is written.

- [x] T001 Create `.streamlit/config.toml` with `[theme] base = "dark"`
- [x] T002 Create `requirements.txt` listing `streamlit`, `pandas`, `plotly`
- [x] T003 [P] Create stub file `data.py` at repo root with module docstring
- [x] T004 [P] Create stub file `charts.py` at repo root with module docstring
- [x] T005 [P] Create stub file `app.py` at repo root with module docstring

---

## Phase 2: Foundational — Data Layer (`data.py`)

**Purpose**: Build the shared data generation module that all user stories depend on.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T006 Write product catalogue constant (dict: category → list of `(product, unit_price)` tuples covering all 5 categories and 15 products) in `data.py`
- [x] T007 [P] Write `_sample_dates(rng, n)` helper that returns `n` random `datetime.date` objects sampled uniformly from 2024-01-01 – 2024-12-31 in `data.py`
- [x] T008 Write `generate_data(seed=42)` function skeleton: initialize `numpy.random.default_rng(seed)` and call `_sample_dates` in `data.py`
- [x] T009 Write order_id column generation (`f"ORD-{i:06d}"` for i in range(n)) inside `generate_data()` in `data.py`
- [x] T010 Write category, product, and region random selection (uniform choice using rng) inside `generate_data()` in `data.py`
- [x] T011 Write quantity generation (`rng.integers(1, 6)` per row) and unit_price lookup from product catalogue inside `generate_data()` in `data.py`
- [x] T012 Write `total_amount` column computation (`quantity × unit_price`) and return final `pd.DataFrame` with 8 columns from `generate_data()` in `data.py`
- [x] T013 Manually validate `generate_data()` returns a DataFrame with columns `[date, order_id, product, category, region, quantity, unit_price, total_amount]` and approximately 1,000 rows

**Checkpoint**: `python -c "from data import generate_data; df = generate_data(); print(df.shape, df.columns.tolist())"` prints `(1000, 8)` with correct column names.

---

## Phase 3: User Story 1 — KPI Cards (Priority: P1) 🎯 MVP

**Goal**: Visitor sees Total Sales and Total Orders at a glance on a dark-themed dashboard.

**Independent Test**: `streamlit run app.py` → two metric cards visible with non-zero dollar and count values.

### Implementation for User Story 1

- [x] T014 [US1] Write `kpi_metrics(df)` in `data.py` that returns a dict with keys `total_sales` (`df["total_amount"].sum()`) and `total_orders` (`df["order_id"].nunique()`)
- [x] T015 [US1] Write `st.set_page_config(page_title="ShopSmart Dashboard", layout="wide")` call at top of `app.py`
- [x] T016 [US1] Write `st.title("ShopSmart Sales Dashboard")` header and one-line subtitle in `app.py`
- [x] T017 [US1] Call `generate_data()` and `kpi_metrics()`, then render two `st.metric()` cards inside `st.columns(2)` in `app.py`
- [x] T018 [US1] Format `total_sales` as a currency string `f"${total_sales:,.0f}"` before passing to `st.metric()` in `app.py`

**Checkpoint**: `streamlit run app.py` → dark background, dashboard title, and two KPI metric cards (Total Sales ≈ $650K–$700K, Total Orders ≈ 480–520).

---

## Phase 4: User Story 2 — Sales Trend Chart (Priority: P2)

**Goal**: Visitor sees monthly revenue trend as a line chart below the KPI cards.

**Independent Test**: `streamlit run app.py` → line chart with exactly 12 data points (Jan–Dec) renders below KPI cards.

### Implementation for User Story 2

- [x] T019 [US2] Write `monthly_trend(df)` in `data.py` that groups by month period (`df["date"].dt.to_period("M")`), sums `total_amount`, and returns a 12-element `pd.Series` with string month labels as index
- [x] T020 [US2] Write `sales_trend_chart(monthly_series)` in `charts.py` that returns a `go.Figure` line chart using `template="plotly_dark"` with x-axis label "Month" and y-axis label "Revenue ($)"
- [x] T021 [US2] Wire `monthly_trend()` + `sales_trend_chart()` into `app.py` and render with `st.plotly_chart(fig, use_container_width=True)`

**Checkpoint**: `streamlit run app.py` → line chart with 12 monthly points visible, dark background, correct axis labels.

---

## Phase 5: User Story 3 — Category Breakdown Chart (Priority: P3)

**Goal**: Visitor sees total revenue per product category as a sorted bar chart.

**Independent Test**: `streamlit run app.py` → bar chart with exactly 5 bars sorted highest to lowest revenue.

### Implementation for User Story 3

- [ ] T022 [US3] Write `category_summary(df)` in `data.py` that groups by `category`, sums `total_amount`, and returns a `pd.Series` sorted descending
- [ ] T023 [US3] Write `category_chart(category_series)` in `charts.py` that returns a `go.Figure` horizontal or vertical bar chart using `template="plotly_dark"` with title "Sales by Category"
- [ ] T024 [US3] Wire `category_summary()` + `category_chart()` into `app.py` and render with `st.plotly_chart()`

**Checkpoint**: `streamlit run app.py` → bar chart with 5 categories (Electronics, Audio, Wearables, Smart Home, Accessories) sorted by revenue, dark theme.

---

## Phase 6: User Story 4 — Regional Breakdown Chart (Priority: P4)

**Goal**: Visitor sees total revenue per geographic region as a sorted bar chart, displayed side-by-side with the category chart.

**Independent Test**: `streamlit run app.py` → bar chart with exactly 4 bars (North, South, East, West) sorted highest to lowest; both bar charts appear in a two-column row.

### Implementation for User Story 4

- [ ] T025 [US4] Write `region_summary(df)` in `data.py` that groups by `region`, sums `total_amount`, and returns a `pd.Series` sorted descending
- [ ] T026 [US4] Write `region_chart(region_series)` in `charts.py` that returns a `go.Figure` bar chart using `template="plotly_dark"` with title "Sales by Region"
- [ ] T027 [US4] Refactor `app.py` to place `category_chart` and `region_chart` side-by-side using `st.columns(2)`
- [ ] T028 [US4] Wire `region_summary()` + `region_chart()` into the second column in `app.py`

**Checkpoint**: `streamlit run app.py` → category and region bar charts displayed in a two-column row, both dark-themed and sorted.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Visual consistency and portfolio readiness across all user stories.

- [ ] T029 [P] Add descriptive chart title to each chart function (`sales_trend_chart`, `category_chart`, `region_chart`) in `charts.py` if not already set
- [ ] T030 [P] Add currency hover tooltip format (`"$%{y:,.0f}"`) to all three chart functions in `charts.py`
- [ ] T031 Verify zero console warnings or deprecation notices during `streamlit run app.py` (check terminal output)
- [ ] T032 Run quickstart.md validation checklist end-to-end and confirm all items pass

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately; T003–T005 run in parallel
- **Foundational (Phase 2)**: Depends on Phase 1 completion — **blocks all user stories**
- **US1 KPI Cards (Phase 3)**: Depends on Phase 2; T014 adds to `data.py`, T015–T018 build `app.py`
- **US2 Trend Chart (Phase 4)**: Depends on Phase 2; can start after US1 checkpoint passes
- **US3 Category Chart (Phase 5)**: Depends on Phase 2; can start after US2 checkpoint passes
- **US4 Region Chart (Phase 6)**: Depends on Phase 2; can start after US3 checkpoint passes
- **Polish (Phase 7)**: Depends on all user story phases; T029–T030 run in parallel

### Parallel Opportunities

```bash
# Phase 1 — run simultaneously:
Task: "Create stub data.py"              # T003
Task: "Create stub charts.py"           # T004
Task: "Create stub app.py"              # T005

# Phase 2 — T007 can run while T006 is being written:
Task: "_sample_dates() helper"          # T007

# Phase 7 — run simultaneously:
Task: "Add chart titles"                # T029
Task: "Add currency tooltips"           # T030
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational data layer
3. Complete Phase 3: KPI cards
4. **STOP and VALIDATE**: Run app → two metric cards visible
5. Deploy to Streamlit Community Cloud as MVP

### Incremental Delivery

1. Setup + Foundational → data layer ready
2. US1 KPI Cards → deploy MVP
3. US2 Trend Chart → deploy
4. US3 Category Chart → deploy
5. US4 Region Chart + Polish → final deploy

---

## Notes

- `[P]` = parallelizable (different files or no shared state)
- `[USn]` maps each task to its user story for traceability
- Each phase checkpoint must pass before the next phase begins
- Every `charts.py` function MUST pass `template="plotly_dark"` to maintain dark theme (Principle I)
- `generate_data()` MUST use `seed=42` as default to ensure reproducibility (Principle II)
