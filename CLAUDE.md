# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is an educational tutorial repository that teaches students a professional AI-assisted development workflow by having them build and deploy a real e-commerce sales dashboard. No production application code lives here — students generate `app.py`, `requirements.txt`, and spec artifacts during the workshop.

## Repository Structure

- `v2/` — Current tutorial: `pre-work-setup.md` (account/tool setup) and `workshop-build-deploy.md` (3-hour build session)
- `v1/` — Original tutorial (8-part reference, superseded by v2)
- `prd/ecommerce-analytics.md` — Product requirements document students use as their starting point
- `data/sales-data.csv` — ~1,000 transaction records (12 months, 5 product categories, 4 regions)

## What Students Build

A Streamlit dashboard displaying KPI scorecards (Total Sales, Total Orders), a sales trend line chart, and bar charts breaking down sales by product category and region. Deployed to Streamlit Community Cloud at a public URL.

## Running the Dashboard (After Workshop)

```bash
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
# venv\Scripts\activate           # Windows
pip install streamlit pandas plotly
streamlit run app.py
# Visit http://localhost:8501
```

Deployment is handled by pushing to GitHub's `main` branch — Streamlit Community Cloud auto-deploys from main.

## Student Workflow (7 Stages)

1. **PRD** — Read `prd/ecommerce-analytics.md` to understand requirements
2. **spec-kit** — Generate constitution, specification, plan, and tasks via `spec-kit`
3. **Jira** — Create trackable issues (project key `ECOM`) from spec-kit tasks
4. **Code** — Build `app.py` and `requirements.txt` using Claude Code + Cursor
5. **Commit** — Save changes with Jira keys in messages (e.g., `ECOM-1: Add KPI scorecards`)
6. **Push** — Upload feature branch to GitHub, open PR, merge to main
7. **Deploy** — Streamlit Community Cloud serves the live dashboard from main

## Artifacts Generated During Workshop

```
specs/001-sales-dashboard/   spec.md, plan.md, tasks.md
.specify/memory/             constitution.md
.claude/commands/            spec-kit slash commands
app.py                       main Streamlit application
requirements.txt             Python dependencies
```

## Technology Stack

| Role | Tool |
|------|------|
| Dashboard framework | Streamlit |
| Data processing | Pandas |
| Charts | Plotly |
| AI assistant | Claude Code (with MCP → Jira) |
| Editor | Cursor |
| Spec planning | spec-kit |
| Issue tracking | Jira (project key: `ECOM`) |
| Hosting | Streamlit Community Cloud |

## Key Concepts

- **Spec-driven development**: Specify WHAT before coding HOW
- **Traceability**: Every commit references a Jira issue key
- **Feature branches**: Develop in isolation, merge to main when complete
- **MCP integration**: Claude Code connects to Jira via Model Context Protocol for in-terminal issue management

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
at `specs/001-sales-dashboard/plan.md`.
<!-- SPECKIT END -->
