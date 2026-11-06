import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("onboarding_funnel_data.csv", parse_dates=["signup_date"])

st.set_page_config(page_title="Funnel Drop-Off Analysis", layout="wide")
st.title("🧭 Funnel Drop-Off Dashboard – SaaS Onboarding Analysis")

# Sidebar filters
with st.sidebar:
    st.header("Filter Users")
    segment = st.multiselect("User Intent Segment", df["user_intent_segment"].unique())
    device = st.multiselect("Device Type", df["device_type"].unique())
    cohort = st.multiselect("Cohort", sorted(df["cohort"].unique()))

filtered = df.copy()
if segment:
    filtered = filtered[filtered["user_intent_segment"].isin(segment)]
if device:
    filtered = filtered[filtered["device_type"].isin(device)]
if cohort:
    filtered = filtered[filtered["cohort"].isin(cohort)]

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Users", f"{filtered.shape[0]:,}")
col2.metric("Funnel Completion Rate", f"{filtered['completed_all_steps'].mean()*100:.1f}%" if filtered.shape[0] > 0 else "0%")
col3.metric("Avg Time to Complete", f"{filtered.loc[filtered["completed_all_steps"] == 1, "total_time_to_complete_sec"].mean()/60:.1f} min" if filtered.loc[filtered["completed_all_steps"] == 1, "total_time_to_complete_sec"].notna().any() else "N/A")
col4.metric("Tooltip Exposure Rate", f"{filtered['tooltip_seen'].mean()*100:.1f}%" if filtered.shape[0] > 0 else "0%")
col5.metric("Blocker Rate", f"{filtered['blocker_event_occurred'].mean()*100:.1f}%" if filtered.shape[0] > 0 else "0%")

# Funnel Drop-Off Chart
st.subheader("📉 Funnel Drop-Off by Step")
step_counts = filtered["drop_off_step"].value_counts().sort_index()
drop_fig = px.bar(
    x=[f"Step {i}" for i in step_counts.index],
    y=step_counts.values,
    labels={"x": "Drop-Off Step", "y": "Users"},
    title="Users by Recorded Drop-Off Step"
)
st.plotly_chart(drop_fig, use_container_width=True)

# Heatmap: Step Time by Segment
st.subheader("⏱️ Avg Time per Step by User Segment")
time_cols = [f"step_{i}_time_sec" for i in range(1, 6)]
step_times = filtered.groupby("user_intent_segment")[time_cols].mean().reset_index()
melted = step_times.melt(id_vars="user_intent_segment", var_name="step", value_name="avg_time_sec")
heatmap = px.density_heatmap(
    melted, x="step", y="user_intent_segment", z="avg_time_sec",
    color_continuous_scale="Blues", title="Average Step Time by User Segment"
)
st.plotly_chart(heatmap, use_container_width=True)

# Retention/Return Rate by Cohort
st.subheader("📆 Completion Rate Over Time (Cohort Tracking)")
cohort_fig = px.line(
    filtered.groupby("cohort")["completed_all_steps"].mean().reset_index(),
    x="cohort", y="completed_all_steps",
    title="Completion Rate by Cohort", labels={"completed_all_steps": "Completion Rate"}
)
st.plotly_chart(cohort_fig, use_container_width=True)

# Boxplot: Total Completion Time by Segment
st.subheader("📦 Time to Complete by Segment")
box_fig = px.box(
    filtered[filtered["completed_all_steps"] == 1],
    x="user_intent_segment", y="total_time_to_complete_sec",
    title="Total Time to Complete by Segment", labels={"total_time_to_complete_sec": "Time (sec)"}
)
st.plotly_chart(box_fig, use_container_width=True)

# Validation and Friction Events
st.subheader("⚠️ UX Friction Events")
friction_fig = px.histogram(
    filtered, x="validation_errors", nbins=10,
    title="Distribution of Validation Errors per User",
    labels={"validation_errors": "Validation Errors"}
)
st.plotly_chart(friction_fig, use_container_width=True)