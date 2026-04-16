import streamlit as st

# --- 1. CONSISTENT PAGE CONFIG ---
st.set_page_config(page_title="About Me | Ma. Rhozeth", layout="wide")

# --- 2. THE UNIFIED SKY BLUE BUBBLES & TRANSPARENT NAV CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1F618D 0%, #3498DB 50%, #87CEEB 100%) !important;
        overflow: hidden;
    }

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

    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebarNav"] li [aria-current="page"] {
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        font-weight: bold;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
    }

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

    .timeline-item {
        border-left: 3px solid #1F618D;
        padding-left: 20px;
        margin-bottom: 15px;
    }

    /* Hobby Card Style */
    .hobby-card {
        background-color: #f8f9f9;
        padding: 15px;
        border-radius: 10px;
        border-top: 3px solid #3498DB;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR CONTENT ---
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

# --- 4. ABOUT ME CONTENT ---
st.title("🧑‍💻 About Me")

# Row 1: Education & Experience
col_edu, col_exp = st.columns([1, 1], gap="large")

with col_edu:
    st.subheader("🎓 Education")
    st.markdown("""
        <div class="timeline-item">
            <h4 style='color: #1F618D; margin-bottom: 0;'>2023 - Present</h4>
            <p><b>BS in Computer Science</b><br>DEBESMSCAT</p>
        </div>
        <div class="timeline-item">
            <h4 style='color: #1F618D; margin-bottom: 0;'>2017 - 2022</h4>
            <p><b>High School Diploma</b><br>Legazpi National High School</p>
        </div>
        <div class="timeline-item">
            <h4 style='color: #1F618D; margin-bottom: 0;'>2010 - 2016</h4>
            <p><b>Elementary Education</b><br>Tagpu Elementary School</p>
        </div>
    """, unsafe_allow_html=True)

with col_exp:
    st.subheader("📈 Achievements")
    st.success("**2025 Hackathon** – 8th Placer")
    st.info("**2024 Digital Arts Competition** – 3rd Place")

st.divider()

# Row 2: Hobbies Section
st.subheader("🎨 Personal Interests & Hobbies")
st.write("Beyond coding, I engage in activities that fuel my creativity and personal growth.")

h_col1, h_col2, h_col3 = st.columns(3)

with h_col1:
    st.markdown("""
        <div class="hobby-card">
            <h4>🎬 Entertainment & Lit</h4>
            <p>Watching movies and reading novels inspire my imagination and allow me to explore different perspectives.</p>
        </div>
    """, unsafe_allow_html=True)

with h_col2:
    st.markdown("""
        <div class="hobby-card">
            <h4>✍️ Creative Arts</h4>
            <p>Writing stories and graphic design serve as my creative outlets, where I share ideas and refine my visual skills.</p>
        </div>
    """, unsafe_allow_html=True)

with h_col3:
    st.markdown("""
        <div class="hobby-card">
            <h4>🍳 Tech & Culinary</h4>
            <p>I enjoy programming challenges to sharpen my mind and experimenting with new recipes in the kitchen.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("""
**Summary:** My hobbies are more than just pastimes; they are essential for my relaxation and continuous learning. 
Whether I'm joining a computer competition or trying a new recipe, I value every experience that helps me grow and enjoy my free time.
""")