import streamlit as st
from dna_engine import DNAEngine

engine = DNAEngine()

st.set_page_config(
    page_title="HYPER-VAULT",
    page_icon="🧬",
    layout="wide"
)

# -------------------------
# Custom CSS Styling
# -------------------------
st.markdown("""
<style>

/* Main app background */
.stApp {
    background: linear-gradient(135deg, #050505, #0d1b2a, #1b263b);
    color: white;
}

/* Title styling */
h1 {
    text-align: center;
    color: #00ffc6;
    font-size: 60px;
}

/* Subtitle */
h3 {
    text-align: center;
    color: #e0e0e0;
}

/* Text areas */
textarea {
    background-color: #0b132b !important;
    color: #00ffc6 !important;
    border-radius: 10px !important;
}

/* Buttons */
button {
    background-color: #00ffc6 !important;
    color: black !important;
    border-radius: 8px !important;
    font-weight: bold !important;
}

/* Upload box */
.css-1cpxqw2 {
    background-color: #0b132b;
    border-radius: 10px;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.title("🧬 HYPER-VAULT")

st.markdown(
"""
### Next-Generation Bio-Digital Data Archiving

Securely convert **Digital Data → DNA Sequence → Recover Original Files**
"""
)

tab1, tab2 = st.tabs(["🔬 Encode File", "🧬 Decode DNA"])

# -------------------------
# ENCODING TAB
# -------------------------
with tab1:

    st.subheader("Upload File to Convert into DNA")

    file = st.file_uploader(
        "Upload a text file",
        type=["txt"]
    )

    if file:

        try:

            dna_data = engine.encode(file.read())

            st.success("File successfully encoded into DNA sequence")

            st.text_area(
                "DNA Sequence",
                dna_data,
                height=220
            )

            st.info(f"DNA Length: {len(dna_data)} letters")

        except Exception as e:

            st.error(f"Encoding error: {str(e)}")


# -------------------------
# DECODING TAB
# -------------------------
with tab2:

    st.subheader("Paste DNA Sequence to Recover File")

    dna_input = st.text_area(
        "Paste DNA sequence (a, c, g, t)",
        height=220
    )

    if st.button("Recover Original File"):

        if dna_input.strip() == "":
            st.warning("Please paste a DNA sequence first")

        else:

            try:

                restored_data = engine.decode(dna_input)

                st.success("DNA verified and decoded successfully")

                st.download_button(
                    label="Download Restored File",
                    data=restored_data,
                    file_name="restored_file.txt",
                    mime="text/plain"
                )

                st.balloons()

            except Exception as e:

                st.error(str(e))
