import streamlit as st
from dna_engine import DNAEngine
import time

engine = DNAEngine()

st.set_page_config(
    page_title="HYPER-VAULT",
    page_icon="🧬",
    layout="wide"
)

# --------------------------
# Animated Background + UI Style
# --------------------------
st.markdown("""
<style>

/* Animated background */
.stApp {
    background: linear-gradient(-45deg, #020617, #0f172a, #1e293b, #020617);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Main container */
.block-container {
    background: rgba(15,23,42,0.75);
    padding: 2rem;
    border-radius: 14px;
    backdrop-filter: blur(10px);
}

/* Title */
h1 {
    text-align: center;
    color: #e2e8f0;
    font-size: 54px;
}

/* Subtitle */
h3 {
    text-align: center;
    color: #cbd5f5;
}

/* Text area styling */
textarea {
    background: #0f172a !important;
    color: #e5e7eb !important;
    border-radius: 10px !important;
}

/* Buttons */
button {
    background: #2563eb !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 17px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# Header
# --------------------------
st.title("🧬 HYPER-VAULT")

st.markdown("""
### Bio-Digital Data Archiving Platform

Securely convert **Digital Files → DNA Sequence → Recover Original Data**
""")

tab1, tab2 = st.tabs(["Encode File", "Decode DNA"])

# --------------------------
# ENCODE
# --------------------------
with tab1:

    st.subheader("Upload File to Convert into DNA")

    file = st.file_uploader("Upload text file", type=["txt"])

    if file:

        with st.spinner("Encoding file into DNA sequence..."):
            time.sleep(1)

            dna_data = engine.encode(file.read())

        st.success("Encoding completed")

        st.text_area(
            "DNA Sequence",
            dna_data,
            height=220
        )

        st.metric(
            "DNA Length",
            f"{len(dna_data)} letters"
        )

# --------------------------
# DECODE
# --------------------------
with tab2:

    st.subheader("Paste DNA Sequence to Recover File")

    dna_input = st.text_area(
        "Paste DNA sequence (a,c,g,t)",
        height=220
    )

    if st.button("Recover Original File"):

        if dna_input.strip() == "":
            st.warning("Please paste DNA sequence")

        else:
            try:

                with st.spinner("Decoding DNA sequence..."):
                    time.sleep(1)

                    restored = engine.decode(dna_input)

                st.success("DNA verified and decoded successfully")

                st.download_button(
                    "Download Restored File",
                    restored,
                    file_name="restored.txt"
                )

            except Exception as e:
                st.error(str(e))
