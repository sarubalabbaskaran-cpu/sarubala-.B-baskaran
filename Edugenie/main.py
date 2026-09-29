from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

# Import your modules - check your file names da
from qna import answer_question_with_gemini
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie")

# Frontend connect
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Query(BaseModel):
    question: str = None
    topic: str = None
    text: str = None

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/qa")
def qa_endpoint(data: Query):
    result = answer_question_with_gemini(data.question)
    return {"answer": result}

@app.post("/explain")
def explain_endpoint(data: Query):
    result = explain_topic(data.topic)
    return {"explanation": result}

@app.post("/quiz")
def quiz_endpoint(data: Query):
    result = generate_quiz(data.text)
    return {"quiz": result}

@app.post("/summarize")
def summarize_endpoint(data: Query):
    result = summarize_text(data.text)
    return {"summary": result}

@app.post("/learn/recommendations")
def learn_endpoint(data: Query):
    result = get_learning_recommendations(data.topic)
    return {"learning_path": result}