import streamlit as st
import math

# --- CLEAN DARK THEME & LAYOUT ---
st.set_page_config(page_title="Hale's Drying Pro", page_icon="🐎", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle, #222222 0%, #0a0a0a 100%);
        color: #ffffff;
    }
    
    /* 3D Glass Cards */
    div[data-testid="stMetric"], .st-emotion-cache-12w0qpk, .st-emotion-cache-1r6slb0 {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px);
        padding: 20px !important;
    }

    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3rem !important;
        background: -webkit-linear-gradient(#ffffff, #777777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px;
    }

    h2, h3 {
        color: #ff8c00 !important; /* Safety Orange */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def calculate_gpp(t, r):
    c = (t - 32) * 5/9
    svp = 6.112 * math.exp((17.67 * c) / (c + 243.5))
    vp = svp * (r / 100)
    return (4354 * vp) / (1013.25 - vp)

# --- HEADER ---
st.markdown('<h1 class="main-title">🐎 HALE\'S RESTORATION PRO</h1>', unsafe_allow_html=True)

# --- GPP SECTION ---
st.subheader("💧 Psychrometrics")
col_a, col_b, col_c = st.columns([2, 2, 1])
with col_a:
    temp = st.slider("Temp (F)", 32, 110, 75)
with col_b:
    rh = st.slider("RH (%)", 0, 100, 45)

gpp = calculate_gpp(temp, rh)
with col_c:
    st.metric("Current GPP", f"{round(gpp, 1)}")

st.divider()

# --- EQUIPMENT SECTION ---
st.subheader("🏗️ IICRC Equipment Set")
c1, c2, c3, c4 = st.columns(4)
with c1:
    l = st.number_input("Length (ft)", value=12)
with c2:
    w = st.number_input("Width (ft)", value=12)
with c3:
    h = st.number_input("Height (ft)", value=8)
with c4:
    water_class = st.selectbox("Water Class", [
        "Class 1 (Minimal)", 
        "Class 2 (Significant)", 
        "Class 3 (Major/Ceiling)", 
        "Class 4 (Hardwood)"
    ])

sq_ft = l * w
cu_ft = sq_ft * h
air_movers = math.ceil(sq_ft / 50)

# Dehu Math
if "Class 1" in water_class:
    divisor = 100
elif "Class 2" in water_class:
    divisor = 40
else:
    divisor = 30

ppd_needed = cu_ft / divisor

# Results Dashboard
res1, res2, res3 = st.columns(3)
with res1:
    st.markdown("### 🌀 Air Movers")
    st.write(f"## {air_movers}")
with res2:
    st.markdown("### 🔋 Dehu PPD")
    st.write(f"## {round(ppd_needed)}")
with res3:
    st.markdown("### 🔥 Scrubbers")
    required_cfm = (cu_ft * 6) / 60
    scrubbers_needed = math.ceil(required_cfm / 500)
    st.write(f"## {scrubbers_needed}")

st.divider()

# --- FIRE & SEALER SECTION ---
low_a, low_b = st.columns(2)
with low_a:
    st.subheader("🛡️ Sealer / Encapsulant")
    surface_area = sq_ft * 3 
    gallons_needed = math.ceil(surface_area / 250)
    st.info(f"**Est. Needed:** {gallons_needed} Gallons")
    st.caption("Covers walls/ceilings (250sqft/gal).")

with low_b:
    st.subheader("📖 IICRC Pro-Tips")
    with st.expander("Water Standards"):
        st.write("""
        * **Class 1:** Small area, easy dry.
        * **Class 2:** Whole room (carpet/pad) wet. 
        * **Class 3:** Water from above or high wick.
        * **Class 4:** Hardwood/Stone/Brick.
        * **Cat 3 (Sewer):** Pad and carpet must be removed.
        """)
    with st.expander("Fire & Smoke"):
        st.write("""
        * **Golden Rule:** Clean surfaces first; you can't kill a smell if soot remains.
        * **Air Changes:** Target 4-6 ACH.
        * **Sealing:** 'Lock' in odors on charred framing.
        * **Don't Mask:** Use Ozone or Hydroxyls to break molecules.
        """)

st.caption("Hale's Drying Progress Calculator v2.0 | Lead Tech Edition")
