
import streamlit as st
import pandas as pd

from modules.fetch_data import get_trend_data
from modules.process_data import analyze_trends
from modules.ai_summary import summarize_trends
from modules.visualize import (
    plot_popular_routes,
    plot_price_heatmap,
    plot_status_pie,
    plot_airline_volume,
    plot_demand_trend  
)

# Streamlit page config
st.set_page_config(page_title="Airline Market Demand", layout="wide")
st.title(" Airline Booking Market Demand Insights")

# Load data
data_load_state = st.text("Loading market data...")
df = get_trend_data()
data_load_state.text("Data loaded successfully!")

if df is not None and not df.empty:
    st.subheader(" Data Preview")
    st.dataframe(df.head())

    # Analyze trends
    insights = analyze_trends(df)

    st.subheader(" Popular Routes")
    st.plotly_chart(plot_popular_routes(insights["popular_routes"]))

    st.subheader(" Search Interest Heatmap")
    st.plotly_chart(plot_price_heatmap(insights["price_trends"]))

    st.subheader(" Daily Search Trend")
    st.plotly_chart(plot_demand_trend(insights["price_trends"]))

    st.subheader(" Flight Volume by Airline")
    st.plotly_chart(plot_airline_volume(df))

    st.subheader(" Booking Status Distribution")
    st.plotly_chart(plot_status_pie(df))

    st.success(" Insights generated successfully!")

    st.subheader(" AI Summary of Trends")
    summary = summarize_trends(insights)
    st.info(summary)

else:
    st.error(" Failed to load or process data. Please try again later.")
