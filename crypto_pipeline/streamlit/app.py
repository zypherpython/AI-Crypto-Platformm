import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st

from ai.read_insights import get_latest_insight
from src.database import get_connection
from src.read_crypto import get_crypto_data
from streamlit_autorefresh import st_autorefresh

st_autorefresh(
    interval=300000,  # 5 minutes (milliseconds)
    key="crypto_refresh"
)

st.set_page_config(
    page_title ="AI Crypto Pipeline",
    page_icon= "📈",
    layout="wide"
)

st.title("📈AI Crypto Pipeline")
st.write("AI-powered cryptocurrency market analysis")

st.divider()

col1,col2 = st.columns(2)

with col1:
    st.subheader("Pipeline")
    st.write("Fetch cryptocurrency market data")
    st.write("Clean and process data")
    st.write("Generate AI insights")

with col2:
    st.subheader("Generate Reports")
    st.subheader("🤖 AI Analysis")

if st.button("Load Latest AI Insight", use_container_width=True):
    insight = get_latest_insight()
    st.markdown(insight)


df = get_crypto_data()

st.subheader("📊 Market Data")

st.dataframe(df, use_container_width=True)
