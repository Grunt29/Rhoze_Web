import streamlit as st

# --- 1. CONSISTENT PAGE CONFIG ---
st.set_page_config(page_title="Technical Skills | Ma. Rhozeth", layout="wide")

# --- 2. THE UNIFIED SKY BLUE BUBBLES & TRANSPARENT NAV CSS ---
st.markdown("""
    <style>
    /* Main Page Reset */
    .stApp {
        background-color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Global Sidebar Style */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1F618D 0%, #3498DB 50%, #87CEEB 100%) !important;
        overflow: hidden;
    }

    /* Consistent Bubble Animation */
    [data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 10%, transparent 10.2%);
        background-size: 50px 50px;
        animation: sidebarBubbles 10s linear infinite;
        z-index: 0;
    }

    @keyframes sidebarBubbles {
        0% { background-position: 0 0; }
        100% { background-position: 0 -500px; }
    }

    /* Sidebar Content Colors */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* TRANSPARENT Navigation Link Highlights */
    [data-testid="stSidebarNav"] li [aria-current="page"] {
        background-color: rgba(255, 255, 255, 0.2) !important; /* Semi-transparent white */
        color: white !important;
        font-weight: bold;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
    }

    /* Unified Circular Profile Image */
    .sidebar-img-container {
        display: flex;
        justify-content: center;
        padding-top: 30px;
        padding-bottom: 10px;
    }
    .sidebar-img-container img {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 3px solid white;
        object-fit: cover;
    }

    /* Glass Effect for Content Blocks */
    [data-testid="stVerticalBlock"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONSISTENT SIDEBAR CONTENT ---
with st.sidebar:
    st.markdown('<div class="sidebar-img-container">', unsafe_allow_html=True)
    try:
        st.image("images/photo.png") 
    except:
        st.write("👤") 
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>Ma. Rhozeth Paz</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 12px;'>Computer Science Student |<br>Web Developer | Graphic Designer</p>", unsafe_allow_html=True)
    st.write("---")

# --- 4. TECHNICAL SKILLS CONTENT ---
st.title("🛠️ Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Web Development")
    st.write("HTML/CSS")
    st.progress(95)
    st.write("Python")
    st.progress(85)
    st.write("PHP & JavaScript")
    st.progress(75)

with col2:
    st.subheader("Graphic Design")
    st.write("Adobe Illustrator")
    st.progress(90)
    st.write("Photoshop & Canva")
    st.progress(95)
    st.write("UI/UX (Figma)")
    st.progress(80)

st.divider()
st.subheader("Other Tools")
t1, t2, t3, t4 = st.columns(4)
with t1:
    st.info("Git & GitHub")
with t2:
    st.info("VS Code")
with t3:
    st.info("MySQL")
with t4:
    st.info("Microsoft Office")