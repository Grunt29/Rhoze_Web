import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Design Portfolio | Ma. Rhozeth", page_icon="🎨", layout="wide")

# --- 2. CONSISTENT SIDEBAR & GLASSMORPHISM CSS ---
st.markdown("""
    <style>
    /* Main Page Reset */
    .stApp {
        background-color: #FFFFFF !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

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

    /* Sidebar Text Colors */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* TRANSPARENT Navigation Highlights */
    [data-testid="stSidebarNav"] li [aria-current="page"] {
        background-color: rgba(255, 255, 255, 0.2) !important; /* Semi-transparent */
        color: white !important;
        font-weight: bold;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
    }

    /* Unified Circular Profile Image sa Sidebar */
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

    /* --- PROJECT CARD EFFECTS WITH TRANSPARENCY --- */
    h1, h2, h3 {
        color: #1F618D; 
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .design-card {
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white card */
        backdrop-filter: blur(5px);
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        width: 100%;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(31, 97, 141, 0.1);
        border-bottom: 5px solid #1F618D;
        margin-bottom: 25px;
    }

    .design-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        background-color: rgba(255, 255, 255, 1); /* Becomes solid on hover */
    }

    .card-image-container img {
        width: 100% !important;
        height: 250px !important;
        object-fit: cover !important; 
    }
    
    .card-content { padding: 25px; }
    .card-title { color: #1F618D; font-size: 20px; font-weight: bold; margin-bottom: 8px; }
    .card-meta { color: #7B7D7D; font-size: 14px; font-weight: 600; margin-bottom: 15px; text-transform: uppercase; }
    .card-description { color: #5D6D7E; font-size: 15px; line-height: 1.6; margin-bottom: 20px; }
    .card-tag { background-color: #EBF5FB; color: #1F618D; padding: 5px 10px; border-radius: 15px; font-size: 12px; font-weight: bold; margin-right: 5px; display: inline-block; }
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

# 4. Page Header
st.title("📂 Project Portfolio")
st.write("Bridging the gap between robust code and elegant visualization.")
st.divider()

# 5. TABS FOR SEPARATION
tab_graphics, tab_certs = st.tabs(["🎨 Graphic Design Portfolio", "📜 Professional Certifications"])

# --- TAB 1: GRAPHICS DESIGN PROJECTS ---
with tab_graphics:
    st.header("Visual Arts & Digital Design Gallery")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        # Synaptic Flow
        st.markdown('<div class="design-card"><div class="card-image-container">', unsafe_allow_html=True)
        st.image("images/helix.jpg", use_container_width=True)
        st.markdown("""
                </div>
                <div class="card-content">
                    <div class="card-title">Synaptic Flow</div>
                    <div class="card-meta">Style: Abstract / Vector | Tools: Adobe Illustrator</div>
                    <p class="card-description">A contemporary abstract composition exploring concepts of digital energy and connectivity.</p>
                    <span class="card-tag">#VectorArt</span><span class="card-tag">#AbstractDesign</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Mandala
        st.markdown('<div class="design-card"><div class="card-image-container">', unsafe_allow_html=True)
        st.image("images/mandala.jpg", use_container_width=True)
        st.markdown("""
                </div>
                <div class="card-content">
                    <div class="card-title">Chromatic Mandala Synthesis</div>
                    <div class="card-meta">Style: Symmetrical Art | Tools: Figma / Canva</div>
                    <p class="card-description">An intricate and symmetrical mandala design built using layered geometric shapes.</p>
                    <span class="card-tag">#Geometric</span><span class="card-tag">#Pattern</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        # PROJECT: Team CODETRIX - Hackathon Season 3
        st.markdown('<div class="design-card"><div class="card-image-container">', unsafe_allow_html=True)
        st.image("images/72eab23d-61c9-403a-a623-0454c5713ab7.jpg", use_container_width=True) 
        st.markdown("""
                </div>
                <div class="card-content">
                    <div class="card-title">Team CODETRIX: Hackathon Season 3</div>
                    <div class="card-meta">Type: Web Development | Event: Hackathon Competition</div>
                    <p class="card-description">Represented DEBESMSCAT as part of Team CODETRIX in a high-intensity web development hackathon, focusing on innovative digital solutions and collaborative coding.</p>
                    <span class="card-tag">#Hackathon</span><span class="card-tag">#Teamwork</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        

    with col2:
        # Photo Manipulation
        st.markdown('<div class="design-card"><div class="card-image-container">', unsafe_allow_html=True)
        st.image("images/photo.jpg", use_container_width=True)
        st.markdown("""
                </div>
                <div class="card-content">
                    <div class="card-title">Surreal Photo Manipulation</div>
                    <div class="card-meta">Style: Conceptual Art | Tools: Adobe Photoshop</div>
                    <p class="card-description">A conceptual composition blending reality and fantasy showcasing mastery in seamless masking.</p>
                    <span class="card-tag">#Photoshop</span><span class="card-tag">#Manipulation</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Low-Poly
        st.markdown('<div class="design-card"><div class="card-image-container">', unsafe_allow_html=True)
        st.image("images/Low-Poly.jpg", use_container_width=True)
        st.markdown("""
                </div>
                <div class="card-content">
                    <div class="card-title">Low-Poly Character Portrait</div>
                    <div class="card-meta">Style: 3D Art / Low-Poly | Tools: Blender 3D</div>
                    <p class="card-description">A stylized 3D low-poly portrait built from simplified polygon networks.</p>
                    <span class="card-tag">#3DArt</span><span class="card-tag">#LowPoly</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        # PROJECT: FitLife Web Portal
        st.markdown('<div class="design-card"><div class="card-image-container">', unsafe_allow_html=True)

        # Ensure your photo is saved as '09f47229-ef10-4ba6-9ca9-ae02e2460591.jpg' in the images folder
        st.image("images/web_deb.jpg", use_container_width=True) 

        st.markdown("""
                </div>
                <div class="card-content">
                    <div class="card-title">FitLife: Bodybuilding Web Portal</div>
                    <div class="card-meta">Type: Web Development | Event: IT Competition</div>
                    <p class="card-description">A web application developed as an academic project at DEBESMSCAT, designed to provide comprehensive fitness guides and bodybuilding resources.</p>
                    <span class="card-tag">#WebDev</span><span class="card-tag">#DEBESMSCAT</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        

# --- TAB 2: CERTIFICATIONS ---
with tab_certs:
    st.header("Technical Certifications")
    st.info("Verified proof of completion for professional courses.")
    cert_col1, cert_col2, cert_col3, cert_col4 = st.columns(4, gap="medium")

    certs = [
        {"title": "Full-Stack Development 101", "url": "images/cert1.jpg"},
        {"title": "Python for Beginners", "url": "images/cert2.jpg"},
        {"title": "Introduction to IoT", "url": "images/cert3.jpg"},
        {"title": "Cisco Packet Tracer", "url": "images/cert4.jpg"},
        {"title": "Web Development", "url": "images/cert5.jpg"},
        {"title": "Build Website with AI", "url": "images/cert6.jpg"},
        {"title": "Google Vid engaging video", "url": "images/cert7.jpg"},
        {"title": "Prompt Engineering", "url": "images/cert8.jpg"},
        {"title": "What is Software development", "url": "images/cert9.jpg"},
        {"title": "Basic of Web Scraping", "url": "images/cert10.jpg"},
    ]

    for index, cert in enumerate(certs):
        current_col = [cert_col1, cert_col2, cert_col3, cert_col4][index % 4]
        with current_col:
            st.markdown('<div style="border:1px solid #EAECEE; padding:10px; border-radius:8px; background-color:rgba(255,255,255,0.7); text-align:center; margin-bottom:10px;">', unsafe_allow_html=True)
            st.image(cert['url'], caption=cert['title'], use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)