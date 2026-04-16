import streamlit as st

# --- 1. CONSISTENT PAGE CONFIG ---
st.set_page_config(page_title="Contact Me | Ma. Rhozeth", page_icon="📬", layout="wide")

# --- 2. THE UNIFIED SKY BLUE BUBBLES & TRANSPARENT NAV CSS ---
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

    /* Sidebar Text & Navigation Color */
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* TRANSPARENT Navigation Link Highlights */
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

    /* Form & Button Styling */
    .stButton>button {
        background-color: #1F618D;
        color: white;
        border-radius: 5px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3498DB;
        border: 1px solid white;
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

# --- 4. CONTACT ME CONTENT ---
st.title("📬 Contact Me")
st.write("I'm always open to new opportunities and collaborations. Feel free to reach out!")

# Centering the form
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Glassy effect box for the form
    st.markdown('<div style="background-color: rgba(240, 248, 255, 0.5); padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0;">', unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            if name and email and message:
                st.success(f"Thank you, {name}! Your message has been sent.")
            else:
                st.error("Please fill out all fields.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Let's Connect")
    
    # Professional layout for contact info
    c1, c2 = st.columns(2)
    
    with c1:
        st.write("👤 **Facebook:** [facebook.com/rhozeth.paz.1](https://www.facebook.com/rhozeth.paz.1)")
    with c2:
        st.write("📧 **Gmail:** pazrhozeth@gmail.com")