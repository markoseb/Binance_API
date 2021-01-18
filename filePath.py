import os
import pandas as pd


THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(THIS_FILE_PATH))
DataFolder = os.path.join(BASE_DIR,"DataFolder/Krypto/data")
dataframe = pd.read_csv(f"{BASE_DIR}/DataFolder/Krypto/conf.txt", sep=";")
API_KEY =dataframe["API_KEY"].item()
API_SECRET = dataframe["API_SECRET"].item()


