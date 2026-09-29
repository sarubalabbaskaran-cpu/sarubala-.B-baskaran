import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_quiz(topic):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
Create a quiz about {topic}.

Give 3 multiple-choice questions.
Each question must have 4 options.
Clearly mention the correct answer.
Keep the questions suitable for a student.
"""
    )

    return response.text