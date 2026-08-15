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
if __name__ == "__main__":
    text=extract_text_from_pdf("resume.pdf")
    extracted_skills=extract_skills(text)
    print("Skills:", extracted_skills)
    print("Skill Score:", calculate_skill_score(extracted_skills))