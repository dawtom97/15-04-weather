import pandas as pd
from config import Config
import os

def save_to_excel(data):

    path = Config.excel_path

    try:
        new_df = pd.DataFrame(data)

        if os.path.exists(path):
            current = pd.read_excel(path)
            concat_data = pd.concat([current, new_df])
            concat_data.to_excel(path, index=False)
        else:
            new_df.to_excel(path, index=False)

    except Exception as e:
        print(e)

# odczytywanie pliku
def read_excel(path):
    try:
        df = pd.read_excel(path)
        return df
    except Exception as e:
        print(e)



