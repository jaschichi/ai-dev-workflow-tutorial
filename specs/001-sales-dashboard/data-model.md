# Data Model: Sales Dashboard

**Date**: 2026-04-19 | **Branch**: `001-sales-dashboard`

## Entities

### Transaction (primary entity)

Represents a single e-commerce order line item. Generated at runtime; never persisted.

| Field | Type | Constraints | Notes |
|-------|------|-------------|-------|
| date | datetime | 2024-01-01 – 2024-12-31 | Sampled from 365 daily dates |
| order_id | str | Unique, format `ORD-XXXXXX` | Sequential 6-digit zero-padded |
| product | str | 15 possible values | See product catalogue below |
| category | str | One of 5 categories | Derived from product |
| region | str | North / South / East / West | Uniform random |
| quantity | int | 1 – 5 | randint inclusive |
| unit_price | float | Category-specific range | See price table below |
| total_amount | float | quantity × unit_price | Computed, not stored separately |

**Total rows**: ~1,000 (exact count reproducible with seed=42)

---

### Product Catalogue (lookup, not a stored entity)

| Category | Products | Price Range |
|----------|----------|-------------|
| Electronics | Laptop, Tablet, Smartphone | $299 – $999 |
| Accessories | Keyboard, Mouse, USB Hub, Cable | $9 – $79 |
| Audio | Wireless Headphones, Earbuds, Speaker | $49 – $199 |
| Wearables | Smartwatch, Fitness Tracker | $99 – $349 |
| Smart Home | Smart Bulb, Smart Plug, Thermostat | $19 – $149 |

---

## Derived Aggregations

These are computed from the Transaction DataFrame at render time — not stored.

### KPI Aggregations

| KPI | Derivation |
|-----|-----------|
| Total Sales | `df["total_amount"].sum()` |
| Total Orders | `df["order_id"].nunique()` |

### Chart Aggregations

| Chart | Grouping | Metric |
|-------|----------|--------|
| Sales Trend | `date` → month period | `total_amount.sum()` per month |
| Category Breakdown | `category` | `total_amount.sum()`, sorted descending |
| Regional Breakdown | `region` | `total_amount.sum()`, sorted descending |

---

## Data Flow

```text
data.py::generate_data(seed=42)
  └─► pd.DataFrame (1,000 rows, 8 columns)
        │
        ├─► app.py: compute KPI scalars (sum, nunique)
        │
        ├─► charts.py::sales_trend_chart(df)
        │     └─► df.groupby(month).sum() → 12-row Series → go.Figure
        │
        ├─► charts.py::category_chart(df)
        │     └─► df.groupby("category").sum().sort_values() → go.Figure
        │
        └─► charts.py::region_chart(df)
              └─► df.groupby("region").sum().sort_values() → go.Figure
```
