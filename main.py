from services.openweather_api import get_weather
from services.excel_files import save_to_excel,read_excel
from services.dashboard import render_dashboard
from services.mysql_db import save_to_mysql, create_db_and_table
from config import Config
import time

# render_dashboard("weather_data.xlsx")

# file = read_excel(Config.excel_path)
# print(file.describe())

create_db_and_table()

while True:
    weather = get_weather()
    save_to_excel([weather])
    save_to_mysql(weather)
    print("Pobrano i zapisano dane")
    time.sleep(5)