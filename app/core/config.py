from dotenv import load_dotenv
import os

load_dotenv()
class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    ALLOWED_ORIGINS = [origin.strip() for origin in os.getenv("ALLOWED_ORIGINS", "").split(",") if origin.strip()]
settings = Settings()