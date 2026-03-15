import streamlit as st
from dna_engine import DNAEngine

# Initialize DNA engine
engine = DNAEngine()

# Page configuration
st.set_page_config(
    page_title="HYPER-VAULT",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 HYPER-VAULT")
st.markdown("### Bio-Digital Data Archiving System")

tab1, tab2 = st.tabs(["Upload & Encode", "Paste & Decode"])

# -------------------------
# ENCODING TAB
# -------------------------
with tab1:

    st.subheader("Step 1: Convert Digital File → DNA")

    uploaded_file = st.file_uploader(
        "Upload a text file",
        type=["txt"],
        key="u1"
    )

    if uploaded_file is not None:

        try:
            file_bytes = uploaded_file.read()

            dna_data = engine.encode(file_bytes)

            st.success("File successfully encoded into DNA sequence")

            st.text_area(
                "DNA Sequence",
                dna_data,
                height=200
            )

            st.info(f"DNA Length: {len(dna_data)} letters")

        except Exception as e:
            st.error(f"Encoding error: {str(e)}")


# -------------------------
# DECODING TAB
# -------------------------
with tab2:

    st.subheader("Step 2: Convert DNA → Digital File")

    dna_input = st.text_area(
        "Paste DNA sequence (a,c,g,t only)",
        height=200,
        key="d1"
    )

    if st.button("Recover Original File"):

        if dna_input.strip() == "":
            st.warning("Please paste a DNA sequence first.")

        else:
            try:

                original_bytes = engine.decode(dna_input)

                st.success("DNA successfully decoded!")

                st.download_button(
                    label="Download Restored File",
                    data=original_bytes,
                    file_name="restored_file.txt",
                    mime="text/plain"
                )

                st.balloons()

            except Exception as e:
                st.error(str(e))
