import streamlit as st
import json

from pdfminer.high_level import extract_text as extract_pdf_text
from openai_utils import analyze_cv_with_gpt 

# Config page
st.set_page_config(
        page_title="CV Analyst",
        page_icon="chart_with_upwards_trend",
        layout="centered",
    )

st.header("CV Analyst 📄")
st.write("Ready to know how much your CV matches a vacancy? Give it a shot")

# --- PARSERS ---
def parse_pdf(file):
    text = extract_pdf_text(file)
    return text

job_title = st.text_input("Job title")
jd_description = st.text_area("Job description", placeholder="Enter the job description")

job_description = "\n".join([job_title, jd_description])

cv_file = st.file_uploader("Upload a CV",  type="pdf")

submit_analysis = st.button("Analyse CV", type="primary", icon="🤖")

if submit_analysis:
    if not cv_file or not job_description:
        st.warning("Please upload a CV and enter a Job Description.")
    else:
        with st.spinner("Analyzing CV..."):
            # CV file.
            if cv_file.name.endswith('.pdf'):
                cv_text = parse_pdf(cv_file)
            
            else:
                st.error("Unsupported file format")
                cv_text = None
            
            if cv_text:
                try:
                    cv_result = analyze_cv_with_gpt(cv_text, job_description)
                    result_json = json.loads(cv_result)
                    
                     # --- Display results ---
                    st.divider()
                    st.subheader("📊 CV Analysis Results")

                    st.metric(label="🔍 Match Score", value=f"{result_json['match_score']}")

                    st.subheader("📌 Missing Skills")
                    if result_json["missing_skills"]:
                        for skill in result_json["missing_skills"]:
                            st.markdown(f"- ❌ **{skill}**")
                    else:
                        st.success("Great! All required skills seem to be covered.")

                    st.subheader("🧠 Summary")
                    st.write(result_json["reasoning"])
                except json.JSONDecodeError:
                    st.error("There was an error parsing GPT's response. Please try again.")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")
            else:
                st.error("Unable to extract text from the CV file.")