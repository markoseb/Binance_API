import pandas as pd
import os
from filePath import DataFolder
import requests
import pprint


def Read_course_from_csv(symbol="USD"):
    """ 
        The function to get current currency rate from Exchange_rates.csv file
  
        Parameters: 
            symbol (str): The symbol to return. 
          
        Returns: 
            current prise:  A current currency rate in PLN
    """

    cvs_file = Read_csv()
    currency_list = cvs_file["currency"]
    # print (currency_list)
    course_list = cvs_file["course"]
    n = 0
    for i in currency_list:
        if i == symbol:
            # print (currency_list)
            return course_list[n].replace(",", ".")
        n = n + 1


def Read_csv(file_name="Exchange_rates"):
    """
        The function to read CSV file and return DataFrame
  
        Parameters: 
            file_name (str): The file name to read 
          
        Returns: 
            file (DataFrame):  A DataFrame file
    """

    filepath = os.path.join(DataFolder, f'{file_name}.csv')
    if os.path.isfile(filepath):
        return pd.read_csv(filepath, encoding='utf-8', sep=';')
    else:
        return False


def Write_csv_file(data_list=[], columns=[], filepath=""):
    """
        The function to write/create CSV file
  
        Parameters: 
            data_list (list): Data List to Add
            columns (list): The names of columns 
            filepath (list): The file name to Create/Edit 
          
        Returns: 
            
    """

    mode = 'a'
    header = False
    if not os.path.isfile(f"{DataFolder}/{filepath}"):
        mode = 'w'
        header = True

    df = pd.DataFrame(data_list, columns=columns)
    df.to_csv(path_or_buf=filepath, index=False, mode=mode, header=header, encoding='utf-8', sep=';')
