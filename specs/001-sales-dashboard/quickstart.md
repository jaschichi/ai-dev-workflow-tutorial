# Quickstart: Sales Dashboard

**Branch**: `001-sales-dashboard` | **Date**: 2026-04-19

## Prerequisites

- Python 3.9+
- Git

## Local Setup

```bash
# Clone and enter the repo
git clone <your-repo-url>
cd ai-dev-workflow-tutorial

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# Install dependencies
pip install streamlit pandas plotly

# Run the dashboard
streamlit run app.py
```

Visit **http://localhost:8501** — the dashboard loads with synthetic data automatically.

## Expected Output

| Metric | Approximate Value |
|--------|------------------|
| Total Sales | ~$650,000 – $700,000 |
| Total Orders | ~480 – 520 |
| Top Category | Electronics or Audio |
| Regions shown | North, South, East, West |

Values are reproducible — the same seed (42) produces the same numbers on every run.

## Dark Theme

The dashboard uses Streamlit's dark theme configured via `.streamlit/config.toml`.
If the theme appears light, confirm the config file is present:

```toml
# .streamlit/config.toml
[theme]
base = "dark"
```

## File Structure

```text
app.py           # Entry point — run this with `streamlit run app.py`
data.py          # Data generation (edit seed here to change data)
charts.py        # Chart builders (edit colors/styles here)
requirements.txt # pip dependencies
.streamlit/
└── config.toml  # Dark theme config
```

## Deployment (Streamlit Community Cloud)

1. Push `main` branch to GitHub
2. Go to share.streamlit.io → New app → select repo → `app.py`
3. Deploy — public URL available within ~2 minutes
4. Every push to `main` auto-redeploys

## Validation Checklist

After running locally, confirm:

- [ ] Two KPI cards visible (Total Sales, Total Orders)
- [ ] Sales trend line chart shows 12 monthly data points
- [ ] Category bar chart shows 5 bars sorted by value
- [ ] Region bar chart shows 4 bars sorted by value
- [ ] Dark theme applied throughout
- [ ] No errors or warnings in terminal
