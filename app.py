import streamlit as st
import matplotlib.pyplot as plt
import re
from io import BytesIO

from utils.pdf_reader import extract_text_from_pdf

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📄 AI Resume Screening System")

st.write(
    "Upload your Resume PDF and compare it with the Job Description."
)

# -----------------------------
# Features
# -----------------------------
st.header("🚀 Project Features")

st.write("""
✅ Upload Resume PDF

✅ Extract Resume Text

✅ Candidate Details

✅ ATS Score

✅ Resume Statistics

✅ Skill Match Percentage

✅ Pie Chart

✅ Bar Chart

✅ Matching Skills

✅ Missing Skills

✅ Resume Rating

✅ Download ATS Report
""")

# -----------------------------
# Upload Resume
# -----------------------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

resume_text = ""

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ Resume Uploaded Successfully")

    st.write("**File Name:**", uploaded_file.name)

    st.subheader("📄 Resume Text")

    st.text_area(
        "Extracted Resume",
        resume_text,
        height=250
    )

    # -----------------------------
    # Candidate Details
    # -----------------------------

    st.subheader("👤 Candidate Details")

    # Candidate Name
    lines = resume_text.split("\n")

    if len(lines) > 0:
        st.write("👤 Name :", lines[0])

    # Email
    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )

    if email:
        st.write("📧 Email :", email[0])

    # Phone
    phone = re.findall(
        r"\+?\d[\d\s-]{8,15}",
        resume_text
    )

    if phone:
        st.write("📱 Phone :", phone[0])

    # LinkedIn
    if "linkedin" in resume_text.lower():
        st.success("✅ LinkedIn Profile Found")
    else:
        st.warning("❌ LinkedIn Profile Not Found")

    # Experience
    experience = re.findall(
        r'(\d+)\+?\s*years?',
        resume_text.lower()
    )

    if experience:
        st.write("💼 Experience :", experience[0], "Years")
    else:
        st.write("💼 Experience : Fresher")

    # Education
    education_list = [
        "B.Tech",
        "B.E",
        "M.Tech",
        "MCA",
        "B.Sc",
        "M.Sc",
        "MBA"
    ]

    found = False

    for edu in education_list:
        if edu.lower() in resume_text.lower():
            st.write("🎓 Education :", edu)
            found = True
            break

    if not found:
        st.write("🎓 Education : Not Found")

# -----------------------------
# Job Description
# -----------------------------

st.subheader("📝 Job Description")

job_description = st.text_area(
    "Paste Job Description Here",
    height=250
)
# -----------------------------
# ATS Score Calculation
# -----------------------------

if uploaded_file is not None and job_description:

    resume = resume_text.lower()
    jd = job_description.lower()

    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "pandas",
        "numpy",
        "tensorflow",
        "opencv",
        "power bi",
        "excel",
        "django",
        "flask"
    ]

    matched = []
    missing = []

    for skill in skills:
        if skill in jd:
            if skill in resume:
                matched.append(skill)
            else:
                missing.append(skill)

    total_skills = len(matched) + len(missing)

    if total_skills > 0:
        score = int((len(matched) / total_skills) * 100)
    else:
        score = 0

    # -----------------------------
    # ATS Score
    # -----------------------------

    st.subheader("📊 ATS Score")

    st.progress(score / 100)

    st.success(f"ATS Score : {score}%")

    # -----------------------------
    # Resume Statistics
    # -----------------------------

    st.subheader("📈 Resume Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATS Score", f"{score}%")

    with col2:
        st.metric("Matched Skills", len(matched))

    with col3:
        st.metric("Missing Skills", len(missing))

    # -----------------------------
    # Skill Match Percentage
    # -----------------------------

    st.subheader("🎯 Skill Match Percentage")

    match_percentage = (
        len(matched) / total_skills
    ) * 100 if total_skills > 0 else 0

    st.progress(match_percentage / 100)

    st.write(f"Skill Match : {match_percentage:.1f}%")

    # -----------------------------
    # Resume Rating
    # -----------------------------

    st.subheader("⭐ Resume Rating")

    if score >= 90:
        st.success("⭐⭐⭐⭐⭐ Excellent Resume")
    elif score >= 80:
        st.success("⭐⭐⭐⭐ Very Good Resume")
    elif score >= 60:
        st.warning("⭐⭐⭐ Good Resume")
    elif score >= 40:
        st.warning("⭐⭐ Average Resume")
    else:
        st.error("⭐ Needs Improvement")
            # -----------------------------
    # Resume Suggestions
    # -----------------------------

    st.subheader("💡 Resume Improvement Suggestions")

    if score < 60:
        st.warning("""
• Add more Python projects

• Learn Django / Flask

• Improve SQL Skills

• Learn TensorFlow

• Mention Power BI

• Improve Resume Keywords
""")
    else:
        st.success("🎉 Your Resume is well optimized!")

    # -----------------------------
    # Pie Chart
    # -----------------------------

    st.subheader("📊 Skill Match Chart")

    labels = ["Matched Skills", "Missing Skills"]
    sizes = [len(matched), len(missing)]
    colors = ["green", "red"]

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

    # -----------------------------
    # Bar Chart
    # -----------------------------

    st.subheader("📊 Skill Comparison Bar Chart")

    fig2, ax2 = plt.subplots()

    ax2.bar(
        ["Matched", "Missing"],
        [len(matched), len(missing)],
        color=["green", "red"]
    )

    ax2.set_ylabel("Number of Skills")
    ax2.set_title("Matched vs Missing Skills")

    st.pyplot(fig2)

    # -----------------------------
    # Matching Skills
    # -----------------------------

    st.subheader("✅ Matching Skills")

    if matched:
        for skill in matched:
            st.success(skill.title())
    else:
        st.info("No Matching Skills Found")

    # -----------------------------
    # Missing Skills
    # -----------------------------

    st.subheader("❌ Missing Skills")

    if missing:
        for skill in missing:
            st.error(skill.title())
    else:
        st.success("🎉 No Missing Skills")

    # -----------------------------
    # Download ATS Report
    # -----------------------------

    st.subheader("📄 Download ATS Report")

    report = f"""
AI Resume Screening Report

ATS Score : {score}%

Matched Skills:
{', '.join(matched)}

Missing Skills:
{', '.join(missing)}
"""

    st.download_button(
        label="📥 Download ATS Report",
        data=report,
        file_name="ATS_Report.txt",
        mime="text/plain"
    )