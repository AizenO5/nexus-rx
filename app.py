import streamlit as st
import pandas as pd

# 1. Page Configuration (Set to Dark Mode by Default)
st.set_page_config(
    page_title="NexusRx | The Silent Guardian",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for "Metallic/CRED" Aesthetic
def local_css():
    cred_style = """
    <style>
        /* Main Background */
        .stApp {
            background-color: #050505;
            color: #E0E0E0;
        }

        /* Metallic Card Design */
        [data-testid="stVerticalBlock"] > div:has(div.metallic-card) {
            background: linear-gradient(145deg, #1a1a1a, #0a0a0a);
            border: 1px solid #333;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 10px 10px 20px #020202, -5px -5px 15px #1e1e1e;
            margin-bottom: 20px;
        }

        /* Metallic Buttons */
        div.stButton > button {
            background: linear-gradient(145deg, #222, #000);
            color: #00ffcc; /* Neon Cyan */
            border: 1px solid #444;
            border-radius: 12px;
            padding: 10px 25px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            box-shadow: 4px 4px 8px #020202, -2px -2px 6px #222;
            transition: all 0.3s ease;
        }

        div.stButton > button:hover {
            border-color: #00ffcc;
            color: #ffffff;
            box-shadow: 0px 0px 15px #00ffcc; /* Neon Glow Effect */
            transform: translateY(-2px);
        }

        /* High Contrast Headers */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            letter-spacing: -1px;
            color: #ffffff;
        }
    </style>
    """
    st.markdown(cred_style, unsafe_allow_html=True)

local_css()

# 3. App Content
st.title("N E X U S R x")
st.caption("THE SILENT GUARDIAN OF THE PHARMACY")

# Example of the "Metallic Card" Layout
col1, col2 = st.columns([2, 1])

with col1:
    with st.container():
        st.markdown('<div class="metallic-card">', unsafe_allow_html=True)
        st.subheader("💊 Search Medicine")
        med_name = st.text_input("Enter Medicine Name (e.g., Azoran 50mg)", placeholder="Start typing...")
        if st.button("HUNT PRICE"):
            st.success(f"Searching for {med_name} across the grid...")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="metallic-card">', unsafe_allow_html=True)
        st.subheader("🛡️ Agent Status")
        st.info("Verification: Active")
        st.info("Price-Hunter: Scanning")
        st.markdown('</div>', unsafe_allow_html=True)