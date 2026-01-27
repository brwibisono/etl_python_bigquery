import pandas as pd
import streamlit as st

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
st.title("📊 E-Commerce Performance Dashboard")

DATA_PATH = "/content/drive/MyDrive/submission/dashboard/main_data.csv"
df = pd.read_csv(DATA_PATH)

df["order_month"] = pd.to_datetime(df["order_month"])

# Sidebar filter
st.sidebar.header("Filter")
min_date = df["order_month"].min()
max_date = df["order_month"].max()

date_range = st.sidebar.date_input(
    "Select date range:",
    value=(min_date.date(), max_date.date()),
    min_value=min_date.date(),
    max_value=max_date.date()
)

start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
df = df[(df["order_month"] >= start_date) & (df["order_month"] <= end_date)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", f"{int(df['orders'].sum()):,}")
col2.metric("Total Revenue", f"{df['revenue'].sum():,.2f}")
col3.metric("Avg Orders / Month", f"{df['orders'].mean():,.1f}")
col4.metric("Avg Revenue / Month", f"{df['revenue'].mean():,.2f}")

st.divider()
st.line_chart(df.set_index("order_month")[["orders", "revenue"]])
st.dataframe(df)
