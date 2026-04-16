import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ma. Rhozeth | Portfolio", 
    page_icon="🎨", 
    layout="wide"
)

st.markdown("""
    <style>
    /* SIDEBAR STYLING - Sky Blue Bubbles */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1F618D 0%, #3498DB 50%, #87CEEB 100%) !important;
        overflow: hidden;
    }

    /* Sidebar Bubble Animation */
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

    /* Sidebar Text & Navigation Color */
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
    
    /* Hover Effect para sa sidebar links */
    [data-testid="stSidebarNav"] li:hover {
        background-color: rgba(255, 255, 255, 0.1) !important;
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

    .sidebar-specialization {
        text-align: center;
        font-size: 12px;
        font-weight: 500;
        line-height: 1.4;
        padding: 0 10px;
        opacity: 0.9;
    }

    /* MAIN CONTENT AREA */
    .stApp {
        background-color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION CONTENT ---
with st.sidebar:
    st.markdown('<div class="sidebar-img-container">', unsafe_allow_html=True)
    try:
        st.image("images/photo.png") 
    except:
        st.write("👤")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>Ma. Rhozeth Paz</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="sidebar-specialization">
            Computer Science Student |<br>Web Developer | Graphic Designer
        </div>
    """, unsafe_allow_html=True)
    st.write("---")

# --- 4. MAIN HOMEPAGE CONTENT (Centered Layout) ---
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Main Welcome Title
    st.markdown("<h1 style='text-align: center; color: #1F618D; font-size: 4rem; font-weight: 800; line-height: 1.1; text-transform: uppercase;'>WELCOME TO MY PORTFOLIO</h1>", unsafe_allow_html=True)

    # Greeting Name
    st.markdown("<h2 style='text-align: center; color: #1F618D; font-weight: 700; font-size: 2.2rem; margin-top: 20px;'>Hi! I'm Ma. Rhozeth</h2>", unsafe_allow_html=True)

    # Comprehensive Description Text
    st.markdown("""
        <p style='text-align: center; font-size: 1.2rem; color: #566573; line-height: 1.6; max-width: 800px; margin: 0 auto; margin-top: 15px;'>
            I am a Computer Science student and creative designer passionate about turning 
            complex ideas into elegant digital solutions. Explore my journey and technical 
            works through the dashboard.
        </p>
    """, unsafe_allow_html=True)

    # Location Section
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold; color: #1F618D; font-size: 1.1rem;'>📍 Masbate, Philippines</p>", unsafe_allow_html=True)