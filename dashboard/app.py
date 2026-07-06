import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ======================================
# Page Configuration
# ======================================

st.set_page_config(
    page_title="Retail Sales Analytics Dashboard",
    layout="wide"
)

st.title("📊 Retail Sales Analytics Dashboard")
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Forecast"
    ]
)

# ======================================
# Database Connection
# ======================================

conn = sqlite3.connect("sales.db")
df = pd.read_sql("SELECT * FROM sales", conn)

# ======================================
# Sidebar Filters
# ======================================

st.sidebar.success("Retail Sales Analytics")
st.sidebar.caption("Interactive Dashboard")

st.sidebar.divider()

st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique())
)

year = st.sidebar.selectbox(
    "Year",
    ["All"] + sorted(df["Year"].astype(str).unique())
)

filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

if year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == int(year)
    ]

if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

if page == "Dashboard":
    # ======================================
    # KPI Cards
    # ======================================

    total_revenue = filtered_df["Revenue"].sum()
    total_profit = filtered_df["Profit"].sum()
    total_orders = len(filtered_df)

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
    col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
    col3.metric("🛒 Total Orders", total_orders)

    st.divider()

    # ======================================
    # Revenue by Category
    # ======================================

    st.subheader("Revenue by Category")

    category_sales = (
        filtered_df.groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        category_sales,
        x="Category",
        y="Revenue",
        color="Category",
        title="Revenue by Category"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ======================================
    # Monthly Revenue Trend
    # ======================================

    st.subheader("Monthly Revenue Trend")

    monthly_sales = (
        filtered_df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    fig2 = px.line(
        monthly_sales,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ======================================
    # Monthly Revenue by Category
    # ======================================

    st.subheader("Monthly Revenue by Category")

    monthly_category = (
        filtered_df
        .groupby(["Month", "Category"])["Revenue"]
        .sum()
        .reset_index()
    )

    fig3 = px.line(
        monthly_category,
        x="Month",
        y="Revenue",
        color="Category",
        markers=True,
        title="Monthly Revenue by Category"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # ======================================
    # Top Customers
    # ======================================

    st.subheader("Top 10 Customers")

    top_customers = (
        filtered_df
        .groupby("Customer_ID")["Revenue"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig4 = px.bar(
        top_customers,
        x="Customer_ID",
        y="Revenue",
        color="Revenue",
        title="Top Customers"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # ======================================
    # Profit Distribution
    # ======================================

    st.subheader("Profit Distribution")

    profit_category = (
        filtered_df
        .groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )

    fig5 = px.pie(
        profit_category,
        names="Category",
        values="Profit",
        title="Profit Distribution"
    )

    st.plotly_chart(fig5, use_container_width=True)

    # ======================================
    # Units Sold by Month
    # ======================================

    st.subheader("Units Sold by Month")

    units_month = (
        filtered_df
        .groupby("Month")["Units_Sold"]
        .sum()
        .reset_index()
    )

    fig6 = px.bar(
        units_month,
        x="Month",
        y="Units_Sold",
        color="Units_Sold",
        title="Units Sold by Month"
    )

    st.plotly_chart(fig6, use_container_width=True)

    # ======================================
    # Average Profit Margin
    # ======================================

    st.subheader("Average Profit Margin")

    avg_margin = (
        filtered_df
        .groupby("Category")["Profit_Margin"]
        .mean()
        .reset_index()
    )

    fig7 = px.bar(
        avg_margin,
        x="Category",
        y="Profit_Margin",
        color="Profit_Margin",
        title="Average Profit Margin"
    )

    st.plotly_chart(fig7, use_container_width=True)

    # ======================================
    # Revenue vs Profit
    # ======================================

    st.subheader("Revenue vs Profit")

    fig8 = px.scatter(
        filtered_df,
        x="Revenue",
        y="Profit",
        color="Category",
        hover_data=["Customer_ID"],
        title="Revenue vs Profit"
    )

    st.plotly_chart(fig8, use_container_width=True)

    # ======================================
    # Revenue Share by Category (Treemap)
    # ======================================

    st.subheader("Revenue Share by Category")

    category_share = (
        filtered_df
        .groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig9 = px.treemap(
        category_share,
        path=["Category"],
        values="Revenue",
        color="Revenue",
        title="Revenue Share by Category"
    )

    st.plotly_chart(fig9, use_container_width=True)

    # ======================================
    # Download Filtered Data
    # ======================================

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Data",
        data=csv,
        file_name="filtered_sales.csv",
        mime="text/csv",
    )

    

    # ======================================
    # Dataset Preview
    # ======================================

    st.subheader("Dataset Preview")

    st.dataframe(
        filtered_df.head(20),
        use_container_width=True
    )

if page == "Forecast":

    st.header("📈 Sales Forecast")

    forecast = pd.read_csv("data/processed/forecast.csv")

    fig10 = px.line(
        forecast,
        x="Month",
        y="Predicted_Revenue",
        markers=True,
        title="Predicted Revenue"
    )

    st.plotly_chart(fig10, use_container_width=True)

    st.dataframe(
        forecast,
        use_container_width=True
    )    

# ======================================
# Close Database Connection
# ======================================
st.divider()

st.caption(
    "Built with ❤️ using Streamlit • Pandas • SQLite • Plotly • Scikit-learn"
)
conn.close()