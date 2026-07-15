import streamlit as st
import re
import matplotlib.pyplot as plt
from utils.pdf_reader import extract_text_from_pdf

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------
# Title
# ---------------------------------------

st.title("📄 AI Resume Screening System")
st.markdown("### Upload your resume and analyze it with AI")
st.divider()

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.title("📌 Project Features")

features = [
    "✅ Upload Resume PDF",
    "✅ Candidate Details",
    "✅ Resume Analysis",
    "✅ Resume Sections",
    "✅ Resume Completeness Score",
    "✅ Recommended Job Roles",
    "✅ Interview Questions",
    "✅ Job Description",
    "✅ ATS Score",
    "✅ Resume Statistics",
    "✅ Skill Match Percentage",
    "✅ Resume Rating",
    "✅ Resume Suggestions",
    "✅ Pie Chart",
    "✅ Bar Chart",
    "✅ Matching Skills",
    "✅ Missing Skills",
    "✅ Skill Gap Analysis",
    "✅ Download ATS Report"
]

for feature in features:
    st.sidebar.write(feature)

# ---------------------------------------
# Feature 1
# Upload Resume
# ---------------------------------------

st.subheader("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("📄 Please upload a PDF resume to continue.")
    st.stop()

resume_text = extract_text_from_pdf(uploaded_file)

st.success("✅ Resume Uploaded Successfully")

# ---------------------------------------
# Feature 2
# Candidate Details
# ---------------------------------------

st.subheader("👤 Candidate Details")

name = "Not Found"
email = "Not Found"
phone = "Not Found"

lines = resume_text.split("\n")

for line in lines:
    line = line.strip()

    if len(line) > 2:
        name = line
        break

email_match = re.search(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    resume_text
)

if email_match:
    email = email_match.group()

phone_match = re.search(
    r"(\+91[- ]?)?[6-9]\d{9}",
    resume_text
)

if phone_match:
    phone = phone_match.group()

col1, col2 = st.columns(2)

with col1:
    st.write("**👤 Name :**", name)
    st.write("**📧 Email :**", email)

with col2:
    st.write("**📱 Phone :**", phone)

st.divider()

# ---------------------------------------
# Feature 3
# Resume Analysis
# ---------------------------------------

st.subheader("📑 Resume Analysis")

word_count = len(resume_text.split())
char_count = len(resume_text)
line_count = len(lines)

st.write("📄 Total Words :", word_count)
st.write("🔤 Total Characters :", char_count)
st.write("📃 Total Lines :", line_count)
# ---------------------------------------
# Feature 4
# Resume Sections
# ---------------------------------------

st.divider()
st.subheader("📂 Resume Sections")

sections = {
    "Education": ["education", "b.tech", "btech", "degree", "college", "university"],
    "Skills": ["skills", "technical skills", "technologies"],
    "Projects": ["project", "projects"],
    "Experience": ["experience", "work experience", "internship"],
    "Certifications": ["certification", "certifications", "certificate"],
    "Achievements": ["achievement", "achievements"],
}

found_sections = []

for section, keywords in sections.items():
    for keyword in keywords:
        if keyword.lower() in resume_text.lower():
            found_sections.append(section)
            break

for section in found_sections:
    st.success(f"✅ {section}")

missing_sections = []

for section in sections.keys():
    if section not in found_sections:
        missing_sections.append(section)

if missing_sections:
    st.warning("Missing Sections")
    for item in missing_sections:
        st.write("❌", item)

# ---------------------------------------
# Feature 5
# Resume Completeness Score
# ---------------------------------------

st.divider()
st.subheader("📈 Resume Completeness Score")

completeness = int((len(found_sections) / len(sections)) * 100)

st.progress(completeness / 100)
st.metric("Completeness", f"{completeness}%")

if completeness >= 90:
    st.success("Excellent Resume")
elif completeness >= 70:
    st.info("Good Resume")
else:
    st.warning("Resume needs improvement")

# ---------------------------------------
# Feature 6
# Recommended Job Roles
# ---------------------------------------

st.divider()
st.subheader("💼 Recommended Job Roles")

text = resume_text.lower()

recommended_roles = []

if "python" in text:
    recommended_roles.append("Python Developer")

if "machine learning" in text or "tensorflow" in text:
    recommended_roles.append("Machine Learning Engineer")

if "artificial intelligence" in text or "ai" in text:
    recommended_roles.append("AI Engineer")

if "sql" in text:
    recommended_roles.append("Data Analyst")

if "power bi" in text:
    recommended_roles.append("Business Intelligence Analyst")

if "html" in text or "css" in text or "javascript" in text:
    recommended_roles.append("Frontend Developer")

if "django" in text:
    recommended_roles.append("Backend Developer")

if len(recommended_roles) == 0:
    recommended_roles.append("Software Engineer")

for role in recommended_roles:
    st.success(role)
    # ---------------------------------------
# Feature 7
# Interview Questions
# ---------------------------------------

st.divider()
st.subheader("🎤 Interview Questions")

questions = [
    "Tell me about yourself.",
    "Explain your final year project.",
    "What are Python Lists and Tuples?",
    "What is Machine Learning?",
    "Explain OOP concepts in Python.",
    "What is NumPy?",
    "What is Pandas?",
    "Explain SQL Joins.",
    "What is Exception Handling?",
    "Difference between List and Dictionary?",
    "Why should we hire you?",
    "What are your strengths?",
    "What are your weaknesses?"
]

for i, q in enumerate(questions, start=1):
    st.write(f"{i}. {q}")

# ---------------------------------------
# Feature 8
# Job Description
# ---------------------------------------

st.divider()
st.subheader("📋 Job Description")

job_description = st.text_area(
    "Paste Job Description Here",
    height=220
)

# ---------------------------------------
# Feature 9
# ATS Score Calculation
# ---------------------------------------

required_skills = []

if job_description.strip() != "":

    jd = job_description.lower()

    skill_database = [
        "python",
        "java",
        "c",
        "c++",
        "sql",
        "mysql",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "django",
        "flask",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "tensorflow",
        "keras",
        "numpy",
        "pandas",
        "opencv",
        "power bi",
        "excel",
        "git",
        "github"
    ]

    for skill in skill_database:
        if skill in jd:
            required_skills.append(skill)

    resume_lower = resume_text.lower()

    matched = []
    missing = []

    for skill in required_skills:

        if skill in resume_lower:
            matched.append(skill)

        else:
            missing.append(skill)

    total_skills = len(required_skills)

    if total_skills == 0:
        ats_score = 0
    else:
        ats_score = round((len(matched) / total_skills) * 100)

else:

    st.info("Paste a Job Description to continue ATS Analysis.")
    st.stop()
    # ---------------------------------------
# Feature 10
# ATS Score
# ---------------------------------------

st.divider()
st.subheader("🎯 ATS Score")

st.progress(ats_score / 100)
st.metric("ATS Score", f"{ats_score}%")

if ats_score >= 80:
    st.success("Excellent Resume Match")
elif ats_score >= 60:
    st.info("Good Resume Match")
else:
    st.warning("Low Resume Match")

# ---------------------------------------
# Feature 11
# Resume Statistics
# ---------------------------------------

st.divider()
st.subheader("📊 Resume Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Words", word_count)

with col2:
    st.metric("Characters", char_count)

with col3:
    st.metric("Skills Found", len(matched))

# ---------------------------------------
# Feature 12
# Skill Match Percentage
# ---------------------------------------

st.divider()
st.subheader("📈 Skill Match Percentage")

match_percentage = ats_score
missing_percentage = 100 - ats_score

col1, col2 = st.columns(2)

with col1:
    st.metric("Matched Skills %", f"{match_percentage}%")

with col2:
    st.metric("Missing Skills %", f"{missing_percentage}%")

st.progress(match_percentage / 100)
# ---------------------------------------
# Feature 13
# Resume Rating
# ---------------------------------------

st.divider()
st.subheader("⭐ Resume Rating")

if ats_score >= 90:
    rating = "★★★★★ Excellent"
elif ats_score >= 75:
    rating = "★★★★☆ Very Good"
elif ats_score >= 60:
    rating = "★★★☆☆ Good"
elif ats_score >= 40:
    rating = "★★☆☆☆ Average"
else:
    rating = "★☆☆☆☆ Needs Improvement"

st.success(f"Resume Rating : {rating}")

# ---------------------------------------
# Feature 14
# Resume Suggestions
# ---------------------------------------

st.divider()
st.subheader("💡 Resume Suggestions")

suggestions = []

if ats_score < 80:
    suggestions.append("Add more skills from the Job Description.")

if "project" not in resume_text.lower():
    suggestions.append("Add Projects section.")

if "certification" not in resume_text.lower():
    suggestions.append("Add Certifications section.")

if "experience" not in resume_text.lower():
    suggestions.append("Add Internship / Experience section.")

if len(suggestions) == 0:
    st.success("🎉 Excellent Resume. No major suggestions.")

else:
    for i, tip in enumerate(suggestions, start=1):
        st.warning(f"{i}. {tip}")

# ---------------------------------------
# Feature 15
# Skill Match Pie Chart
# ---------------------------------------

st.divider()
st.subheader("🥧 Skill Match Pie Chart")

labels = ["Matched Skills", "Missing Skills"]

sizes = [
    len(matched),
    len(missing)
]

colors = ["green", "red"]

explode = (0.08, 0)

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

ax.axis("equal")

st.pyplot(fig)
# ---------------------------------------
# Feature 16
# Skill Match Bar Chart
# ---------------------------------------

st.divider()
st.subheader("📊 Skill Match Bar Chart")

fig, ax = plt.subplots(figsize=(6,4))

categories = ["Matched", "Missing"]
values = [len(matched), len(missing)]

ax.bar(
    categories,
    values,
    color=["green", "red"],
    width=0.5
)

ax.set_ylabel("Number of Skills")
ax.set_title("Matched vs Missing Skills")

for i, value in enumerate(values):
    ax.text(i, value + 0.2, str(value), ha="center")

st.pyplot(fig)

# ---------------------------------------
# Feature 17
# Matching Skills
# ---------------------------------------

st.divider()
st.subheader("✅ Matching Skills")

if len(matched) == 0:
    st.warning("No Matching Skills Found")
else:

    col1, col2 = st.columns(2)

    for index, skill in enumerate(matched):

        if index % 2 == 0:
            with col1:
                st.success(skill.title())

        else:
            with col2:
                st.success(skill.title())
                # ---------------------------------------
# Feature 18
# Missing Skills
# ---------------------------------------

st.divider()
st.subheader("❌ Missing Skills")

if len(missing) == 0:
    st.success("Excellent! No Missing Skills")
else:

    col1, col2 = st.columns(2)

    for index, skill in enumerate(missing):

        if index % 2 == 0:
            with col1:
                st.error(skill.title())

        else:
            with col2:
                st.error(skill.title())

# ---------------------------------------
# Feature 19
# Skill Gap Analysis
# ---------------------------------------

st.divider()
st.subheader("📉 Skill Gap Analysis")

matched_count = len(matched)
missing_count = len(missing)

st.write(f"### ✅ Matched Skills : {matched_count}")
st.write(f"### ❌ Missing Skills : {missing_count}")

if total_skills > 0:
    gap_percentage = round((missing_count / total_skills) * 100, 2)
else:
    gap_percentage = 0

st.metric("Skill Gap", f"{gap_percentage}%")

if gap_percentage == 0:
    st.success("🎉 Your resume matches all required skills.")
elif gap_percentage <= 20:
    st.info("Good! Only a few skills are missing.")
elif gap_percentage <= 50:
    st.warning("Moderate skill gap. Add more relevant skills.")
else:
    st.error("High skill gap. Update your resume according to the Job Description.")

if missing_count > 0:

    st.write("### 📌 Skills to Learn")

    for skill in missing:
        st.write(f"➡️ {skill.title()}")
        # ---------------------------------------
# Feature 20
# Download ATS Report
# ---------------------------------------

st.divider()
st.subheader("📥 Download ATS Report")

report = f"""
===============================
AI RESUME SCREENING REPORT
===============================

Candidate Name : {name}
Email          : {email}
Phone          : {phone}

--------------------------------
Resume Statistics
--------------------------------

Words          : {word_count}
Characters     : {char_count}
Lines          : {line_count}

--------------------------------
ATS Result
--------------------------------

ATS Score              : {ats_score}%
Resume Rating          : {rating}
Skill Match Percentage : {match_percentage}%

--------------------------------
Matched Skills
--------------------------------

{chr(10).join(matched)}

--------------------------------
Missing Skills
--------------------------------

{chr(10).join(missing)}

--------------------------------
Recommended Job Roles
--------------------------------

{chr(10).join(recommended_roles)}

--------------------------------
Interview Questions
--------------------------------

{chr(10).join(questions)}

===============================
Generated by
AI Resume Screening System
===============================
"""

st.download_button(
    label="📄 Download ATS Report",
    data=report,
    file_name="ATS_Report.txt",
    mime="text/plain"
)

st.success("🎉 AI Resume Screening System Completed Successfully!")