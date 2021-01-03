import os
from pathlib import Path

import pytesseract
from dotenv import load_dotenv

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv("tesseract_path")

Path("output").mkdir(parents=True, exist_ok=True)
