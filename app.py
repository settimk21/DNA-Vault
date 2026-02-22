import streamlit as st
from dna_engine import DNAEngine

engine = DNAEngine()

st.set_page_config(page_title="HYPER-VAULT", page_icon="🧬")

st.title("🧬 HYPER-VAULT")
st.markdown("### Bio-Digital Data Archiving")

tab1, tab2 = st.tabs(["Upload & Encode", "Paste & Decode"])

# ------------------ ENCODE TAB ------------------
with tab1:
    st.subheader("Step 1: Digital to DNA")

    file = st.file_uploader("Upload your test.txt file here", key="u1")

    if file:
        dna_data = engine.encode(file.read())
        st.success("Successfully encoded!")
        st.text_area("Your DNA Sequence:", dna_data, height=150)

# ------------------ DECODE TAB ------------------
with tab2:
    st.subheader("Step 2: DNA to Digital")

    dna_input = st.text_area("Paste the DNA letters here:", height=200, key="d1")

    if st.button("Recover Original File", key="b1"):
        if dna_input:
            try:
                original_bytes = engine.decode(dna_input)
                st.download_button(
                    "Download Restored File",
                    original_bytes,
                    file_name="restored.txt"
                )
                st.balloons()
            except:
                st.error("Invalid DNA sequence.")