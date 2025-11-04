import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-production-secret-key-change-this'
    
    # Database - will be set via environment variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload settings
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
    
    # AI/ML settings
    YOLO_MODEL_PATH = 'static/models/best.pt'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    CONFIDENCE_THRESHOLD = 0.5
