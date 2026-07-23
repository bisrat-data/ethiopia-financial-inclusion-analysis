import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_excel("data/raw/ethiopia_fi_unified_data.xlsx")

# -----------------------------
# TITLE
# -----------------------------
st.title("🇪🇹 Ethiopia Financial Inclusion Dashboard")
st.markdown("Financial Inclusion Analysis for Ethiopia")
st.markdown("""
This dashboard analyzes financial inclusion indicators in Ethiopia.

Use the filters on the left to explore data by:

- Pillar
- Category
- Fiscal Year
- Gender
- Indicator

The charts update automatically based on your selections.
""")

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

selected_pillars = st.sidebar.multiselect(
    "Select Pillar",
    options=sorted(df["pillar"].dropna().unique())
)

selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].dropna().unique())
)

selected_years = st.sidebar.multiselect(
    "Select Fiscal Year",
    options=df["fiscal_year"].dropna().astype(str).unique()
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].dropna().astype(str).unique()
)

search_indicator = st.sidebar.text_input(
    "Search Indicator"
)

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_df = df.copy()

if selected_pillars:
    filtered_df = filtered_df[
        filtered_df["pillar"].isin(selected_pillars)
    ]

if selected_categories:
    filtered_df = filtered_df[
        filtered_df["category"].isin(selected_categories)
    ]

if selected_years:
    filtered_df = filtered_df[
        filtered_df["fiscal_year"].astype(str).isin(selected_years)
    ]

if selected_gender:
    filtered_df = filtered_df[
        filtered_df["gender"].isin(selected_gender)
    ]

if search_indicator:
    filtered_df = filtered_df[
        filtered_df["indicator"]
        .astype(str)
        .str.contains(search_indicator, case=False, na=False)
    ]

# -----------------------------
# KPI CARDS
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "📄 Records",
    len(filtered_df)
)

col2.metric(
    "📊 Indicators",
    filtered_df["indicator"].nunique()
)

col3.metric(
    "🏷 Categories",
    filtered_df["category"].nunique()
)

col4.metric(
    "🏛 Pillars",
    filtered_df["pillar"].nunique()
)

col5.metric(
    "👥 Genders",
    filtered_df["gender"].nunique()
)

st.divider()

# -----------------------------
# Records by Pillar
st.subheader("📊 Records by Pillar")

pillar_counts = (
    filtered_df["pillar"]
    .value_counts()
    .reset_index()
)

pillar_counts.columns = ["Pillar", "Count"]

if not pillar_counts.empty:

    fig = px.bar(
        pillar_counts,
        x="Pillar",
        y="Count",
        title="Records by Pillar"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No data available for selected filters.")

# -----------------------------
# Records by Category
st.subheader("📊 Records by Category")

category_counts = (
    filtered_df["category"]
    .value_counts()
    .reset_index()
)

category_counts.columns = ["Category", "Count"]

if not category_counts.empty:

    fig = px.bar(
        category_counts,
        x="Category",
        y="Count",
        title="Records by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No data available for selected filters.")

st.subheader("🥧 Category Distribution")

pie_data = (
    filtered_df["category"]
    .value_counts()
    .reset_index()
)

pie_data.columns = ["Category", "Count"]

fig = px.pie(
    pie_data,
    names="Category",
    values="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("👥 Gender Distribution")

gender_counts = (
    filtered_df["gender"]
    .fillna("Unknown")
    .value_counts()
    .reset_index()
)

gender_counts.columns = ["Gender", "Count"]

fig = px.bar(
    gender_counts,
    x="Gender",
    y="Count",
    title="Records by Gender"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📚 Record Types")

record_counts = (
    filtered_df["record_type"]
    .fillna("Unknown")
    .value_counts()
    .reset_index()
)

record_counts.columns = ["Record Type", "Count"]

fig = px.pie(
    record_counts,
    names="Record Type",
    values="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("🌐 Data Sources")

source_counts = (
    filtered_df["source_name"]
    .fillna("Unknown")
    .value_counts()
    .head(10)
    .reset_index()
)

source_counts.columns = ["Source", "Count"]

fig = px.bar(
    source_counts,
    x="Source",
    y="Count",
    title="Top Data Sources"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("🗺 Regional Distribution")

region_counts = (
    filtered_df["region"]
    .fillna("Unknown")
    .value_counts()
    .reset_index()
)

region_counts.columns = ["Region", "Count"]

fig = px.bar(
    region_counts,
    x="Region",
    y="Count",
    title="Records by Region"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# INDICATOR VALUES
# -----------------------------
st.subheader("📈 Average Indicator Values")

numeric_df = filtered_df.dropna(subset=["value_numeric"])

if not numeric_df.empty:

    indicator_avg = (
        numeric_df.groupby("indicator")["value_numeric"]
        .mean()
        .sort_values(ascending=False)
    )

    st.bar_chart(indicator_avg)

else:
    st.warning("No numeric values available.")

# -----------------------------
# Financial Inclusion Trend by Year
st.subheader("📈 Financial Inclusion Trend by Year")

year_df = filtered_df.copy()

year_df["fiscal_year"] = year_df["fiscal_year"].astype(str)

trend_data = (
    year_df.dropna(subset=["value_numeric"])
    .groupby("fiscal_year")["value_numeric"]
    .mean()
    .reset_index()
)

trend_data.columns = ["Year", "Average Value"]

if not trend_data.empty:

    fig = px.line(
        trend_data,
        x="Year",
        y="Average Value",
        markers=True,
        title="Average Financial Inclusion Indicator by Year"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No year trend data available.")

st.subheader("🔗 Correlation Analysis")

numeric_cols = filtered_df.select_dtypes(
    include=["number"]
)

if numeric_cols.shape[1] > 1:

    corr = numeric_cols.corr(
        numeric_only=True
    )

    st.dataframe(corr)

else:
    st.info(
        "Not enough numeric columns for correlation analysis."
    )

# -----------------------------
# INDICATOR SUMMARY
# -----------------------------
st.subheader("📋 Indicator Summary")

if not numeric_df.empty:

    summary = (
    numeric_df.groupby("indicator")["value_numeric"]
    .agg(["count", "mean", "min", "max"])
    .sort_values("mean", ascending=False)
    .round(2)
)

    st.dataframe(summary)

st.subheader("🏆 Top Indicators")

if not numeric_df.empty:

    top_indicators = (
        numeric_df.groupby("indicator")["value_numeric"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    st.dataframe(top_indicators)

# -----------------------------
# Data Preview Table
with st.expander("📋 View Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# Download filtered data
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=csv,
    file_name="ethiopia_financial_inclusion.csv",
    mime="text/csv"
)

# -----------------------------
# DATASET INFORMATION
# -----------------------------
with st.expander("📌 Dataset Information"):

    col1, col2 = st.columns(2)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))

    st.write("Column Names:")
    st.write(list(df.columns))

    st.divider()

st.markdown(
    """
    **Ethiopia Financial Inclusion Dashboard**

    Built with:
    - Streamlit
    - Pandas
    - Plotly

    Author: Netsanet Gebrekidan
    """
)