import os

class Config:
    VECTOR_DB_PATH = "./vector_store/chromadb"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-xxxxx")
