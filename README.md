# 🧭 Funnel Drop-Off Analysis – SaaS Onboarding Dashboard

This project simulates the onboarding funnel of a Grammarly-style SaaS product to analyze where users drop off and why. It includes step timing, UX blockers, and intent-based segments (Trial vs Paid) to uncover user friction.

## 📊 Features
- KPI Cards: Completion Rate, Avg Time to Complete, Tooltip CTR, Blocker Rate
- Filters: User Intent, Device Type, Cohort
- Visuals:
  - Drop-Off by Step
  - Avg Step Time by Segment (Heatmap)
  - Funnel Completion by Cohort
  - Box Plot: Time to Complete by Segment
  - Histogram: Validation Errors per User

## 🧪 Use Cases
- Diagnose onboarding drop-off
- Identify friction caused by tooltips, blockers, or validation errors
- Measure impact of trial vs paid behavior
- Track cohort performance over time

## 🛠 Tools Used
- Python
- Streamlit
- Pandas
- Plotly

## 🚀 How to Run
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

## 📁 Files
- `app.py`: Streamlit dashboard
- `onboarding_funnel_data.csv`: Simulated dataset
- `requirements.txt`: Project dependencies
- `funnel_case_study.docx`: Case study summary