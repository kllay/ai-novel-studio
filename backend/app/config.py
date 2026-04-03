from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')
    DEBUG: bool = os.getenv('DEBUG', 'true').lower() == 'true'
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    API_TITLE: str = 'AI Novel Studio API'
    API_VERSION: str = '1.0.0'
    
    DATABASE_URL: str = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:root@localhost:3306/ai_novel_studio'
    )
    REDIS_URL: str = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'your-secret-key')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    OLLAMA_BASE_URL: str = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
    OLLAMA_MODEL: str = os.getenv('OLLAMA_MODEL', 'qwen:7b-chat-q4_0')
    
    ALLOWED_ORIGINS: list = [
        'http://localhost:3000',
        'http://localhost:5173',
    ]
    
    class Config:
        env_file = '.env'

settings = Settings()