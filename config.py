import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration settings"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://username:password@localhost/driver_inspection_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload settings
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
    
    # AI/ML settings
    YOLO_MODEL_PATH = 'static/models/best.pt'
    
    # OpenAI API Key - with validation
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    if not OPENAI_API_KEY or OPENAI_API_KEY.startswith('your-openai-api-key'):
        print("WARNING: OpenAI API key not properly configured in .env file")
        print("Please set OPENAI_API_KEY=your_actual_api_key in .env file")
    
    # Processing settings
    CONFIDENCE_THRESHOLD = 0.5  # Minimum confidence for YOLO detection