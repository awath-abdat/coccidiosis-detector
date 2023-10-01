from dotenv import load_dotenv
from pathlib import Path
import os

PATH = Path(__file__).parent
load_dotenv()

MODEL_FILE_URL = os.getenv('MODEL_FILE_URL')
MODEL_FILE_NAME = os.getenv('MODEL_FILE_NAME')
MODEL_PATH = PATH/'models/chickens.h5'
TEMPORARY_IMAGE_FILE_PATH = '/tmp/saved_image.png'