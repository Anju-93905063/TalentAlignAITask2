# app.py
import streamlit as st
from main import extract_text, preprocess, calculate_similarity

st.set_page_config(page_title="TalentAlign AI", layout="wide")
st.title("TalentAlign AI: Streamlining Talent Discovery with Intelligent Resume Matching")

st.markdown("**Batch - 1**")
st.markdown("""
### Task:
1. Remove extra spaces, symbols, stopwords  
2. Convert text to lowercase  
3. Replace common abbreviations (e.g., “JS” → “JavaScript”)
""")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type="pdf", key="resume")
with col2:
    jd_file = st.file_uploader("📄 Upload Job Description (PDF)", type="pdf", key="jd")

if resume_file and jd_file:
    # Save uploaded files locally
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    with open("uploaded_jd.pdf", "wb") as f:
        f.write(jd_file.read())

    # Extract raw text
    resume_text = extract_text("uploaded_resume.pdf")
    jd_text = extract_text("uploaded_jd.pdf")

    # Preprocess text
    resume_clean = preprocess(resume_text)
    jd_clean = preprocess(jd_text)

    # Calculate similarity score
    score = calculate_similarity(resume_clean, jd_clean)

    # Display Results
    st.markdown("---")
    st.subheader("📘 Resume Raw Text")
    st.text_area("Raw Resume Text", resume_text, height=200)

    st.subheader("🧹 Resume Cleaned Text")
    st.text_area("Cleaned Resume Text", resume_clean, height=200)

    st.subheader("📗 JD Raw Text")
    st.text_area("Raw JD Text", jd_text, height=200)

    st.subheader("🧹 JD Cleaned Text")
    st.text_area("Cleaned JD Text", jd_clean, height=200)

    st.markdown("### ✅ Match Score:")
    st.success(f"📊 Resume-JD Match Score: **{score:.2f}** (out of 1.0)")
