from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    """Application configuration with environment variable support"""
    
    # Groq API Keys (replacing Gemini)
    groq_api_key: str
    groq_api_key_2: str = ""
    serp_api_key: str
    tavily_api_key: str = ""  # Optional
    webscraping_ai_api_key: str = "" # For AI-powered Review Extraction
    
    # Application
    environment: Literal["development", "production"] = "development"
    database_path: str = "./data/checkpoints.db"
    log_level: str = "INFO"
    
    # LLM Settings
    llm_model: str = "llama-3.3-70b-versatile"  # Groq's best model
    llm_temperature: float = 0.7
    max_tokens: int = 2048
    
    # Agent Settings
    max_iterations: int = 3
    recursion_limit: int = 50
    
    # SerpStack API
    serp_api_url: str = "http://api.serpstack.com/search"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
