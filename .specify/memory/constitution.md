<!--
SYNC IMPACT REPORT
==================
Version change: (blank template) → 1.0.0
New constitution — all principles and sections are net-new additions.

Added sections:
  - Core Principles (5 principles)
  - Tech Stack Constraints
  - Development & Release Workflow
  - Governance

Templates reviewed:
  - .specify/templates/plan-template.md   ✅ no changes needed; Constitution Check section is generic
  - .specify/templates/spec-template.md   ✅ no changes needed; template is project-agnostic
  - .specify/templates/tasks-template.md  ✅ no changes needed; task format is project-agnostic

Follow-up TODOs: none — all placeholders resolved.
-->

# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. Visual Polish (NON-NEGOTIABLE)

Every chart, layout, and UI element MUST look professional and portfolio-ready at all times.
Placeholder text, broken charts, unstyled components, and debug artifacts MUST NOT appear in
any deployed or demo-able state. Design decisions are driven by what impresses a general
public audience encountering the dashboard for the first time.

### II. Simulated Data

All data MUST be generated at runtime using seeded pseudo-random values (e.g., `numpy.random.seed`
or `random.seed`). No external databases, live APIs, CSV file uploads, or environment-specific
data sources are permitted. Seeded generation ensures reproducible, consistent output across
all deployments.

### III. Minimal Dependencies

The technology stack MUST remain lean: Streamlit, Pandas, and Plotly are the only permitted
runtime dependencies unless a new dependency is explicitly justified and documented. Avoid
adding libraries that duplicate functionality already available in the approved stack.

### IV. Iterative, Demo-Ready Increments

Every merged increment MUST leave the dashboard in a fully functional, publicly demonstrable
state. Features are added in layers (P1 → P2 → P3). A half-finished feature MUST NOT be
merged to `main`; use feature branches and merge only when the increment is independently
showcasable.

### V. Portfolio Readiness at All Times

The `main` branch MUST always represent a state the author is proud to share with the general
public. This means: no `TODO` comments in rendered output, no console errors visible to users,
consistent color schemes and typography, and a README that accurately describes what is deployed.

## Tech Stack Constraints

- **Framework**: Streamlit (no raw Flask/FastAPI/Django)
- **Data processing**: Pandas only (no Spark, Dask, or heavyweight alternatives)
- **Visualization**: Plotly only (no Matplotlib, Altair, or Bokeh unless justified in writing)
- **Data source**: Runtime-generated, seeded synthetic data (see Principle II)
- **Hosting**: Streamlit Community Cloud, auto-deployed from `main`
- **Python**: 3.9+ (match Streamlit Community Cloud runtime)

## Development & Release Workflow

- Work in feature branches; branch names follow `###-short-description` convention.
- Every commit that touches `app.py` or `requirements.txt` MUST result in a locally runnable
  dashboard before pushing.
- Merges to `main` trigger auto-deploy; verify the live URL within 5 minutes of merge.
- Each iteration cycle: branch → build → visual QA → merge → verify deploy.
- Changelogs are maintained in commit messages, not in separate files, unless explicitly requested.

## Governance

This constitution supersedes all other informal conventions for this project. Amendments require:
1. A clear rationale tied to one of the five principles or a gap they leave.
2. A version bump following semantic versioning (MAJOR: principle removal/redefinition;
   MINOR: new principle or section; PATCH: clarification or wording).
3. Propagation checks across all `.specify/templates/` files after any amendment.

All feature specifications and implementation plans MUST include a Constitution Check confirming
compliance with Principles I–V before work begins.

**Version**: 1.0.0 | **Ratified**: 2026-04-19 | **Last Amended**: 2026-04-19
