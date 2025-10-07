from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ResumeText(BaseModel):
    text: str


@app.post("/extract_skills")
def extract_skills(data: ResumeText):
    text = data.text.lower()
    skills = []
    for skill in ["python", "sql", "excel", "aiogram", "fastapi", "ml", "docker"]:
        if skill in text:
            skills.append(skill)
    return {"skills": skills}
