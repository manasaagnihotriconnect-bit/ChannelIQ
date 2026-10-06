import streamlit as st

st.set_page_config(
    page_title="ChannelIQ",
    page_icon="📺",
    layout="wide"
)

st.title("📺 ChannelIQ")
st.subheader("TV Serial Content, TRP & Competitive Intelligence")

st.divider()

serial_name = st.text_input(
    "Enter Serial Name",
    placeholder="Example: Jagadhatri"
)

if st.button("Analyse Serial"):

    if serial_name:

        st.success(f"Research initiated for: {serial_name}")

        st.header("Serial Overview")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Channel", "Researching...")
        col2.metric("Language", "Researching...")
        col3.metric("Genre", "Researching...")
        col4.metric("Status", "Researching...")

        st.divider()

        st.header("Research Modules")

        col1, col2, col3 = st.columns(3)

        col1.info("📖 Content Analysis\n\nComing next")
        col2.info("📊 TRP Intelligence\n\nComing next")
        col3.info("🏆 Competitor Analysis\n\nComing next")

    else:
        st.warning("Please enter a serial name.")
