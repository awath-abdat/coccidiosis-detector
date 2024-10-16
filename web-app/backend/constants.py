import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
PATH = Path(__file__).parent

GOOGLE_CREDENTIALS_FILE = (
    PATH
    / "credentials/client_secret_584713777907-5sr66buubkabf86gtgjo30kcrsfei07o.apps.googleusercontent.com.json"
)

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")
ALLOWED_METHODS = os.getenv("ALLOWED_METHODS", "").split(",")

MODEL_FILE_URL = os.getenv("MODEL_FILE_URL")
MODEL_FILE_NAME = os.getenv("MODEL_FILE_NAME")
MODEL_PATH = PATH / "models/chickens.keras"

TEMPORARY_IMAGE_FILE_PATH = "/tmp/saved_image.png"
