import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set up page configuration
st.set_page_config(page_title="MerchandiseMetrics Dashboard", layout="wide")

# Title Section
st.title("MerchandiseMetrics")

# Subheader for explanation
st.subheader("Real-time insights into merchandise performance and sponsorship ROI.")

# Create mock data
sponsors = ["Nike", "Adidas", "Coca-Cola", "Pepsi", "Puma"]
roi_data = [25, 30, 20, 15, 35]
live_mentions = [500, 450, 300, 200, 150]
social_posts = [200, 180, 140, 120, 100]
merch_sales = [1000, 1200, 800, 500, 600]

# Metrics Section
st.markdown("### Key Performance Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Top Sponsor ROI", "35% (Puma)")
col2.metric("Live Mentions", "500")
col3.metric("Social Posts", "200")
col4.metric("Merch Sales", "$1K")

# Bar Chart: ROI by Sponsor
st.markdown("### Sponsor ROI Performance")
roi_df = pd.DataFrame({"Sponsor": sponsors, "ROI (%)": roi_data})
fig_bar = px.bar(
    roi_df,
    x="Sponsor",
    y="ROI (%)",
    title="ROI by Sponsor",
    color="Sponsor",
    text="ROI (%)",
    template="plotly_dark",
)
st.plotly_chart(fig_bar, use_container_width=True)

# Line Chart: Live Mentions Trend
st.markdown("### Live Mentions During Games")
time_data = pd.date_range("2023-01-01", periods=100, freq="D")
live_mentions_trend = np.random.randint(200, 800, 100)
trend_df = pd.DataFrame({"Date": time_data, "Live Mentions": live_mentions_trend})
fig_line = px.line(
    trend_df,
    x="Date",
    y="Live Mentions",
    title="Live Mentions Over Time",
    template="plotly_dark",
)
st.plotly_chart(fig_line, use_container_width=True)

# Sponsor Breakdown Section
st.markdown("### Sponsor Performance Breakdown")
col1, col2 = st.columns(2)

# Pie Chart: Social Posts by Sponsor
with col1:
    st.markdown("#### Social Posts Distribution")
    pie_df = pd.DataFrame({"Sponsor": sponsors, "Social Posts": social_posts})
    fig_pie = px.pie(
        pie_df,
        names="Sponsor",
        values="Social Posts",
        title="Social Posts by Sponsor",
        template="plotly_dark",
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Merch Sales Data
with col2:
    st.markdown("#### Merch Sales ($)")
    sales_df = pd.DataFrame({"Sponsor": sponsors, "Sales ($)": merch_sales})
    fig_sales = px.bar(
        sales_df,
        x="Sponsor",
        y="Sales ($)",
        title="Merch Sales by Sponsor",
        color="Sponsor",
        text="Sales ($)",
        template="plotly_dark",
    )
    st.plotly_chart(fig_sales, use_container_width=True)

# Call-to-Action Section
st.markdown("### Explore Opportunities")
st.button("Partner with Top Sponsors")
st.button("View Merchandise Insights")

# Footer Section
st.markdown("---")
st.markdown("© 2025 MerchandiseMetrics Dashboard")
§
