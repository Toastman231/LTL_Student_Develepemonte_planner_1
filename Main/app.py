import streamlit as st
import runpy
from pathlib import Path

st.set_page_config(page_title="LTL Pathfinder (Basic)", layout="wide")

dashboard_path = Path(__file__).parent / "ui" / "dashboard.py"
runpy.run_path(dashboard_path)
