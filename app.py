from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "AC_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ashley Chinyanganya"
PAGE_ICON = "random"
NAME = "Ashley Chinyanganya"
DESCRIPTION = """
Systems Engineer. With a great passion for Enterprise network troubleshooting in Satellite communication environments!
"""
EMAIL = "johndoe@email.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCSPNi0mnOprNZSv0DRtXeEQ",
    "LinkedIn": "https://www.linkedin.com/in/ashley-c-3a6152186",
    "GitHub": "https://github.com/afroash",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 FastApi CRUD Using MongoDB -- Understand CRUD principles and was able to create a working API": "https://github.com",
    "🏆 ContainerLab Learning Lab - Setup a functional lab with Cisco XRv, Juniper MXv routers and switchs.":"Coming Soon!!!!",
    "🏆 Ground Network Engineering - Understand the basics of ground network engineering": "Coming Soon!",
    "🏆 VesselFinder - Simple CRUD app the allows you to gather detail for a vessel, such as IP, Current Location.": "Coming Soon",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years Network expereince troubleshooting from Small vessel networks to Satellite Ground Station communication.
- ✔️ Strong hands on experience and knowledge in Cisco and Juniper products.
- ✔️ Good understanding of systems engineering principles.
- ✔️ Good understanding of networking concepts and protocols.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Networking: Cisco CCNP-Encor, Juniper, 
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, Grafana
- 🗄️ Databases: Postgres, MongoDB
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**System Engineer | E2e Group**")
st.write("10/2023 - Present")
st.write(
    """
- ► VV&T testing with Sattelite provider, testing Multicast IPTV service on different earo terminals.
- ► Lease and collaborate with different teams and vendors to ensure working viable product is delivered to end customer.
- ► Identify any new bugs in network system causing packet loss or interuption to required specs
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Ground Network Engineer | Eutelsat Group - OneWeb**")
st.write("01/2022 - 10/2023")
st.write(
    """
- ► Supported the Ground Operations team, provided RF, IP and operational maintenance of the Ground Network. 
- ► Leased with vendors on site with required support and provided access to antenna systems
- ► Reported any issues via our ServiceNow platform following ITIL Framework. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Snr Solutions Engineer | Satcom Global*")
st.write("04/2016 - 01/2022")
st.write(
    """
- ► Designed customer LAN environments for maritime customers allowing seamless access to Global VSAT network
- ► Provided 3rd Level Technical Support to our Support Teams
- ► Assisted Snr Network Engineer managing and provisioning new customers services and our VPN links with our different Satellite Providers. 
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")