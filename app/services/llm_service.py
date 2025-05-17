from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_gpt(question_asked: str) -> str:
    preamble = (

       """You are KilimoGPT, a helpful assistant specialized in farming in Kenya. 
You are an expert agricultural advisor. When a user asks a question about farming, provide a clear, practical, and detailed answer covering:
- Best farming practices
- Crop selection and care
- Pest and disease management
- Soil and water management
- Harvesting and storage tips

Only answer questions related to agriculture in Kenya.  
Respond in either English or Swahili, matching the language used in the user's question.  
Do not repeat the answer in both languages, only respond in one.
"""
    )
    full_prompt = preamble + question_asked
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=full_prompt
        )
        return response.text or "No response received."
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "An error occurred while generating a response."


