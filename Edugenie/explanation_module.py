from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def explain_topic(topic):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Explain this topic in simple words for a student: {topic}"
    )

    return response.text