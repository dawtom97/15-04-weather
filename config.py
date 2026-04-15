import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    api_key = os.getenv("API_KEY")
    api_city = os.getenv("API_CITY")
    excel_path = os.getenv("EXCEL_PATH")