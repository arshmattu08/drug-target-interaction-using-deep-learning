#
import streamlit as st

st.set_page_config(page_title="DTA Predictor", layout="centered")

# loading css and applying it.
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("frontend/styles.css")


# Body content
st.markdown('<div class="title">DTA Predictor</div>', unsafe_allow_html=True)


st.text_input(label="Drug Name")
st.text_input(label="Protein Name")
st.button(label= "Predict Affinity")
st.text("Note: LogIC50 is used as proxy for binding affinity.")


# postprocessed data received shown below

# should include logic50 value and (Weak, Moderate, Strong) message with appropriate colors.

