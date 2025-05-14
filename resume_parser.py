import re

def extract_skills(text, skills_list):
    text = text.lower()
    found_skills = [skill for skill in skills_list if skill.lower() in text]
    return list(set(found_skills))

def extract_experience_years(text):
    match = re.findall(r'(\d+)\+?\s+years?', text.lower())
    return max([int(m) for m in match], default=0)
