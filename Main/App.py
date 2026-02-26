import streamlit as st
import sys
from pathlib import Path

# Add project root so "ui" imports work on Streamlit Cloud
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))


st.set_page_config(page_title="LTL Pathfinder (Basic)", layout="wide")


