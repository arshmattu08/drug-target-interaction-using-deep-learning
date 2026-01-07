#
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(page_title="DTA Predictor", layout="centered")

# loading css and applying it.
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("frontend/styles.css")


# Body content
st.markdown('<div class="title">Drug-Protein Binding Affinity Prediction</div>', unsafe_allow_html=True)


drug = st.text_input(label="Drug SMILES")
protein = st.text_input(label="Protein Sequence")
predict_button = st.button(label= "Predict Affinity")
st.text("Note: LogIC50 is used as proxy for binding affinity.")
st.text("Note: Inital run may take up to a minute.")



# postprocessed data received shown below

# should include logic50 value and (Weak, Moderate, Strong) message with appropriate colors.
API_URL = os.getenv("API_URL")

if predict_button:
    if not drug or not protein:
        st.warning("Please enter both Drug SMILES and Protein Sequence.")
    else:
        response = requests.post(
            API_URL,
            json={
                "drug_smiles": drug,
                "protein_sequence": protein
            },
            timeout=120
        )

        prediction = response.json()["prediction"]
        if response.status_code == 200:
            st.markdown(
            f"""
             <div class="success-box">
             Prediction: {prediction} 
             </div>
            """,
            unsafe_allow_html=True)

            if prediction <= 5.25:
                label, css_class = "Weak", "weak"
            elif prediction <= 5.5:
                 label, css_class = "Moderately Weak", "moderately-weak"
            elif prediction <= 5.75:
                label, css_class = "Moderate", "moderate"
            elif prediction <= 6.25:
                label, css_class = "Moderately Strong", "moderately-strong"
            else:
                label, css_class = "Strong", "strong"

            st.markdown(
            f"""
            <div class="{css_class}">
             {label}
            </div>
             """,
             unsafe_allow_html=True)
        else:
            st.error(response.text)



# Weak <= 5.25
# Moderately Weak  5.25 to 5.5
# Moderate  5.5 5o 5.75
# Moderately Strong 5.75 to 6.25
# Strong > 6.25 