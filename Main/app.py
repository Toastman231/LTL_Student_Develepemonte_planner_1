import streamlit as st
import sys
from pathlib import Path

# Make sure the Main folder is on Python path (Cloud-safe)
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from ui.dashboard import render

st.set_page_config(page_title="LTL Pathfinder (Basic)", layout="wide")
render()
