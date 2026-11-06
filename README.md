# Funnel Drop Off Analysis

**Portfolio case study | Synthetic data | Python, pandas, Streamlit, Plotly**

## Business question
Investigate onboarding friction, incomplete journeys, validation errors, and cohort differences.

## Analyst approach
1. Define the operational decision and measurable KPIs.
2. Segment the simulated records using dashboard controls.
3. Compare trends and flag exceptions for investigation.
4. Check metric definitions and filter consistency before presenting findings.

## Dashboard and metrics
The Streamlit app provides interactive filters, KPI summaries, and charts. Run it locally to explore how the selected segments change the results. The data is **synthetic**: findings are demonstrations of analytical methods, not observed customer outcomes.

## Quality assurance and interpretation
Tooltip exposure is not click-through rate. Completion time is calculated among completed journeys. Drop-off-step counts reflect the source field, not a sequential survival funnel.

**Validation checklist:** confirm the dataset loads; verify KPI numerators/denominators against pandas calculations; test each filter alone and combined; check zero-row and zero-denominator selections; confirm every chart responds to the same filtered dataset; review charts for misleading causal claims.

## Tools and reproduction
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```
The CSV in this repository is simulated sample data. The original case-study document is retained as a supplemental artifact; this README documents the current analytical approach.

## What this demonstrates
Business problem framing, KPI design, data exploration, operational reporting, dashboard development, and analytical QA. This is an independent portfolio exercise, not a client engagement or production deployment.
