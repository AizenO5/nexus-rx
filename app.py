import streamlit as st
import pandas as pd
from agents.price_agent import hunt_best_deal

# 1. Page Configuration (Set to Dark Mode by Default)
st.set_page_config(
    page_title="NexusRx | The Silent Guardian",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for "Metallic/CRED" Aesthetic & New MMT-Style Components
def local_css():
    cred_style = """
    <style>
        /* Main Background */
        .stApp {
            background-color: #050505;
            color: #E0E0E0;
        }

        /* Metallic Card Design (Container) */
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

        /* --- NEW STYLES FOR MMT LAYOUT --- */

        /* The Red Out-Of-Stock Banner */
        .oos-banner {
            background-color: #3d0505;
            border: 1px solid #ff4444;
            color: #ffcccc;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(255, 68, 68, 0.1);
        }
        
        /* The Horizontal Listing Card (Like MMT/Hotels) */
        .listing-card {
            background: linear-gradient(90deg, #121212 0%, #1a1a1a 100%);
            border: 1px solid #333;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            display: flex; /* Horizontal Layout */
            align-items: center;
            justify-content: space-between;
            transition: transform 0.2s, border-color 0.2s;
        }
        
        .listing-card:hover {
            border-color: #00ffcc;
            transform: scale(1.01);
            box-shadow: 0 4px 15px rgba(0, 255, 204, 0.1);
        }
        
        /* Price Tag Style */
        .price-tag {
            font-size: 1.5rem;
            color: #00ffcc;
            font-weight: bold;
            text-shadow: 0 0 5px rgba(0, 255, 204, 0.3);
        }
        
        /* Badge Style (Best Value/Fastest) */
        .badge {
            background-color: #00ffcc;
            color: #000;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
            text-transform: uppercase;
            margin-left: 10px;
        }
        
        /* Store Type Label */
        .store-type {
            color: #888;
            font-size: 0.9rem;
            margin-top: 5px;
        }
    </style>
    """
    st.markdown(cred_style, unsafe_allow_html=True)

local_css()

# 3. App Content & Layout
st.title("N E X U S R x")
st.caption("THE SILENT GUARDIAN OF THE PHARMACY")

# --- TOP SEARCH SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    with st.container():
        st.markdown('<div class="metallic-card">', unsafe_allow_html=True)
        st.subheader("💊 Search Medicine")
        # User Input
        med_name = st.text_input("Enter Medicine Name (e.g., Azoran 50mg)", placeholder="Start typing...")
        
        search_triggered = False
        if st.button("HUNT PRICE"):
            search_triggered = True
        
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="metallic-card">', unsafe_allow_html=True)
        st.subheader("🛡️ Agent Status")
        st.info("Verification: Active")
        st.info("Price-Hunter: Scanning")
        st.markdown('</div>', unsafe_allow_html=True)


# --- RESULTS SECTION (The MMT Style Layout) ---
if search_triggered:
    if med_name:
        with st.spinner(f"Agent 'Hunter' is infiltrating the grid for {med_name}..."):
            # CALL THE AGENT (Returns JSON now)
            data = hunt_best_deal(med_name)
            
            # --- ERROR HANDLING ---
            if "error" in data:
                st.error("⚠️ Agent Malfunction: Unable to parse pricing data.")
                with st.expander("See technical details"):
                    st.write(data)
                st.stop()

            # --- RENDER RESULTS ---
            st.markdown("---")
            
            # Split Layout: Left Panel (Info) vs Right Panel (Feed)
            col_side, col_feed = st.columns([1, 2.5]) 

            # ------------------------------------------------
            # LEFT PANEL: Medicine Summary (Sticky-ish)
            # ------------------------------------------------
            with col_side:
                st.markdown('<div class="metallic-card">', unsafe_allow_html=True)
                info = data.get('medicine_info', {})
                
                # Medicine Header
                st.markdown(f"## 💊 {info.get('name', 'Unknown Medicine')}")
                
                # Composition
                if info.get('composition'):
                    st.markdown(f"**Composition:**")
                    st.caption(f"*{info.get('composition')}*")
                
                st.markdown("---")
                
                # Agent Verdict Box
                st.markdown("### 🤖 Agent Verdict")
                st.info(data.get('agent_verdict', 'No verdict provided.'))
                st.markdown('</div>', unsafe_allow_html=True)

            # ------------------------------------------------
            # RIGHT PANEL: The Price Feed (Listings)
            # ------------------------------------------------
            with col_feed:
                # 1. OUT OF STOCK LOGIC (Red Banner)
                if info.get('is_out_of_stock_everywhere'):
                    st.markdown(f"""
                    <div class="oos-banner">
                        ⚠️ CRITICAL SHORTAGE: {info.get('name')} is OUT OF STOCK globally.
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if info.get('alternative_suggested'):
                        st.warning(f"💡 Agent Recommendation: Showing listings for **{info.get('alternative_suggested')}** instead.")

                # 2. LISTINGS LOOP
                listings = data.get('listings', [])
                
                if not listings:
                    st.warning("No listings found matching your criteria.")
                
                for item in listings:
                    # Logic for badges and styling
                    badge_html = f'<span class="badge">{item["badge"]}</span>' if item.get('badge') else ""
                    
                    # Logic for Out of Stock visual (dimmed opacity)
                    is_oos = item.get('stock_status') == "Out of Stock"
                    opacity = "0.5" if is_oos else "1.0"
                    status_color = "#ff4444" if is_oos else "#44ff44"
                    
                    # Construct the HTML Card
                    card_html = f"""
                    <div class="listing-card" style="opacity: {opacity};">
                        <div>
                            <div style="font-size: 1.2rem; font-weight: bold; color: white; display: flex; align-items: center;">
                                {item.get('store_name')} {badge_html}
                            </div>
                            <div class="store-type">
                                {item.get('type')} • <span style="color: {status_color}; font-weight: bold;">{item.get('stock_status')}</span>
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div class="price-tag">₹{item.get('price')}</div>
                            <div style="font-size: 0.8rem; color: #aaa;">per unit</div>
                        </div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)

    else:
        st.warning("Please enter a medicine name to proceed.")