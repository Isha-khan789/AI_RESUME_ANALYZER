from resume_parser import extract_text_from_pdf
skills = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "React",
    "Node.js",
    "Flask",
    "Django",
    "TensorFlow",
    "Keras",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "SQL",
    "MongoDB",
    "Git",
    "Machine Learning",
    "Deep Learning"
]

def extract_skills(text):
    extracted_skills=[]
    for skill in skills:
        if skill.lower() in text.lower():
            extracted_skills.append(skill)
    return extracted_skills 
def calculate_skill_score(extracted_skills):
    score=len(extracted_skills)*5
    score=min(score,50)
    return score
def calculate_section_score(text):
    score = 0
    text = text.lower()

    if "education" in text:
        score += 15

    if "projects" in text:
        score += 15

    if "experience" in text:
        score += 10

    if "certifications" in text or "certification" in text:
        score += 10

    return score
def find_missing_skills(extracted_skills):
    missing_skills = []

    for skill in skills:
        if skill not in extracted_skills:
            missing_skills.append(skill)

    return missing_skills
def match_job_description(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in skills:
        if skill.lower() in job_description:
            if skill.lower() in resume_text:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

    return matched_skills, missing_skills

if __name__ == "__main__":
    text = extract_text_from_pdf("resume.pdf")

    extracted_skills = extract_skills(text)

    skill_score = calculate_skill_score(extracted_skills)
    section_score = calculate_section_score(text)
    total_score = skill_score + section_score

    missing_skills = find_missing_skills(extracted_skills)

    print("Skills:", extracted_skills)
    print("Missing Skills:", missing_skills)
    print("Skill Score:", skill_score)
    print("Section Score:", section_score)
    print("Total Score:", total_score)
    job_description = """
We are looking for an AI/ML Engineer with Python,
TensorFlow, Keras, Pandas, NumPy and Scikit-learn.
"""

matched, missing = match_job_description(text, job_description)

print("Matched Skills:", matched)
print("Missing Job Skills:", missing)
