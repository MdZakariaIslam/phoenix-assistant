import os
import streamlit as st
from google import genai
from PIL import Image

# Page Configuration
st.set_page_config(page_title="PHOENIX OS", page_icon="🔥", layout="wide")

# Custom CSS for Clean Sci-Fi Grid Layout
st.markdown("""
    <style>
    .stApp {
        background-color: #02050e;
        color: #00f3ff;
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: #040914;
        border-right: 1px solid rgba(0, 243, 255, 0.2);
    }
    .phoenix-card {
        background: rgba(0, 243, 255, 0.02);
        border: 1px solid rgba(0, 243, 255, 0.25);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 12px;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.03);
    }
    .core-reactor {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 2px dashed rgba(0, 243, 255, 0.4);
        border-radius: 50%;
        width: 220px;
        height: 220px;
        margin: 0 auto;
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.2);
        animation: pulse 3s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 15px rgba(0, 243, 255, 0.2); }
        50% { box-shadow: 0 0 35px rgba(0, 243, 255, 0.5); }
        100% { box-shadow: 0 0 15px rgba(0, 243, 255, 0.2); }
    }
    .stTextInput input, .stFileUploader {
        background-color: #040914 !important;
        color: #00f3ff !important;
        border-radius: 8px !important;
        border: 1px solid rgba(0, 243, 255, 0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

# API Key নিরাপদভাবে লোড করার ব্যবস্থা (GitHub Push Protection এড়ানোর জন্য)
api_key = None
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.environ.get("GEMINI_API_KEY")

# Sidebar Control
with st.sidebar:
    st.markdown("### 🔥 PHOENIX SYSTEM")
    st.markdown("<p style='color: #00f3ff; font-size: 0.8rem;'>STATUS: ONLINE v5.0</p>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MODULES", ["PHOENIX-01 (Command)", "PHOENIX-02 (Content Studio)", "PHOENIX-03 (Telemetry)"])
    st.markdown("---")
    st.markdown("**OPERATOR:** Phoenix Master")
    st.markdown("<p style='color:#00ffcc;'>SECURE LINK: ACTIVE</p>", unsafe_allow_html=True)

# Top Bar Header
col_h1, col_h2, col_h3 = st.columns([1, 2, 1])
with col_h1:
    st.markdown("<h4 style='color: #00f3ff; margin:0;'>PHOENIX OS</h4>", unsafe_allow_html=True)
with col_h2:
    st.markdown("<h2 style='text-align: center; color: #00f3ff; text-shadow: 0 0 12px rgba(0,243,255,0.6); margin:0;'>P.H.O.E.N.I.X. // COMMAND CENTER</h2>", unsafe_allow_html=True)
with col_h3:
    st.markdown("<p style='text-align: right; color: rgba(0,243,255,0.8); margin:0;'>LIVE<br>SECURE // UK</p>", unsafe_allow_html=True)

st.markdown("---")

if menu == "PHOENIX-02 (Content Studio)":
    st.subheader("🤖 PHOENIX-02 // Multi-Agent Content Studio")
    niche = st.text_input("ভিডিওর টপিক বা নিশ লিখুন:", "Tech & AI")
    
    if st.button("🚀 Run Content Agents"):
        if not api_key:
            st.error("API Key পাওয়া যায়নি! অনুগ্রহ করে Streamlit Secrets বা Environment Variable-এ GEMINI_API_KEY সেট করুন।")
        else:
            client = genai.Client(api_key=api_key)
            with st.spinner("Agent 1: আইডিয়া তৈরি করছে..."):
                res_1 = client.models.generate_content(
                    model='gemini-3.8-flash',
                    contents=f"Generate 5 viral YouTube video ideas for the niche: {niche}."
                )
                ideas = res_1.text
            st.markdown('<div class="phoenix-card">', unsafe_allow_html=True)
            st.markdown("### 💡 Agent 1: Generated Ideas")
            st.write(ideas)
            st.markdown('</div>', unsafe_allow_html=True)

            with st.spinner("Agent 2: সেরা আইডিয়া বেছে নিয়ে স্টোরি লিখছে..."):
                res_2 = client.models.generate_content(
                    model='gemini-3.8-flash',
                    contents=f"Pick the best idea from below and write an engaging video storyline:\n{ideas}"
                )
                story = res_2.text
            st.markdown('<div class="phoenix-card">', unsafe_allow_html=True)
            st.markdown("### 🎬 Agent 2: Selected Storyline")
            st.write(story)
            st.markdown('</div>', unsafe_allow_html=True)

            with st.spinner("Agent 3: প্রয়োজনীয় রিসার্চ ও ইনফরমেশন রেডি করছে..."):
                res_3 = client.models.generate_content(
                    model='gemini-3.8-flash',
                    contents=f"Provide key facts and research data needed to make a video on:\n{story}"
                )
            st.markdown('<div class="phoenix-card">', unsafe_allow_html=True)
            st.markdown("### 🔍 Agent 3: Research & Info")
            st.write(res_3.text)
            st.markdown('</div>', unsafe_allow_html=True)

else:
    # 3-Column Grid Layout
    left_col, center_col, right_col = st.columns([1.2, 2, 1.2])

    with left_col:
        st.markdown('<div class="phoenix-card">', unsafe_allow_html=True)
        st.markdown("<b>PHOENIX-03 // TELEMETRY</b>", unsafe_allow_html=True)
        st.progress(0.23, text="CPU LOAD: 23%")
        st.progress(0.42, text="CORE TEMP: 42°C")
        st.progress(0.45, text="RAM USAGE: 1.8GB / 4G")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phoenix-card">', unsafe_allow_html=True)
        st.markdown("<b>NETWORK LINK</b>", unsafe_allow_html=True)
        st.write("Host: Raspberry Pi 4")
        st.write("Status: Connected (Secure)")
        st.markdown('</div>', unsafe_allow_html=True)

    with center_col:
        st.markdown("""
            <div class="core-reactor">
                <h3 style="color: #00f3ff; margin:0; text-shadow: 0 0 10px #00f3ff;">PHOENIX</h3>
                <p style="font-size: 0.8rem; color: rgba(0,243,255,0.7); margin:0;">CORE ONLINE</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("")
        
        uploaded_file = st.file_uploader("Upload Image or Video", type=["jpg", "png", "jpeg", "mp4"])
        if uploaded_file is not None:
            if uploaded_file.type.startswith("image"):
                st.image(Image.open(uploaded_file), caption="Visual Input", use_column_width=True)
            elif uploaded_file.type.startswith("video"):
                st.video(uploaded_file)

        prompt = st.text_input("ENTER COMMAND FOR PHOENIX:", placeholder="কী সাহায্য করতে পারি, স্যার?")
        if prompt:
            if not api_key:
                st.error("API Key পাওয়া যায়নি! অনুগ্রহ করে Streamlit Secrets-এ GEMINI_API_KEY সেট করুন।")
            else:
                client = genai.Client(api_key=api_key)
                with st.spinner("PHOENIX PROCESSING COMMAND..."):
                    try:
                        response = client.models.generate_content(
                            model='gemini-3.8-flash',
                            contents=prompt,
                        )
                        st.success("RESPONSE:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"ERROR: {e}")

    with right_col:
        st.markdown('<div class="phoenix-card">', unsafe_allow_html=True)
        st.markdown("<b>ENVIRONMENT</b>", unsafe_allow_html=True)
        st.markdown("<h2>16°C &nbsp;☁️</h2>", unsafe_allow_html=True)
        st.write("Location: United Kingdom")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="phoenix-card">', unsafe_allow_html=True)
        st.markdown("<b>PENDING TASKS</b>", unsafe_allow_html=True)
        st.checkbox("Verify GPIO touch screen", value=True)
        st.checkbox("Run Multi-Agent pipeline", value=False)
        st.checkbox("Deploy on Streamlit Cloud", value=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: rgba(0,243,255,0.5); font-size: 0.8rem;'>PHOENIX ADVANCED PERSONAL ASSISTANT // OPERATING SYSTEM</p>", unsafe_allow_html=True)
