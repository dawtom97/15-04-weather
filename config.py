import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    api_key = os.getenv("API_KEY")
    api_city = os.getenv("API_CITY")
    excel_path = os.getenv("EXCEL_PATH")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")