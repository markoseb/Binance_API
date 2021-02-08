from requests_html import HTML
import requests
import os
import datetime
import sys
import pandas as pd
from filePath import DataFolder


def url_to_file(url="https://kursy-walut.mybank.pl/", filename='2020', save=True):
    """
        The function to read url and create html file
  
        Parameters: 
            url (str): The url adress to get
            filename (str): The name of new html file 
            save (bool): True - create new html file
          
        Returns: 
            html_text(str): string html file
    """

    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        # print(html_text)
        if save:
            with open(f'{DataFolder}\world-{filename}.html', 'w', encoding='utf8', errors="ignore") as f:
                f.write(html_text)
        return html_text
    return None


def parse_and_extract(url, name='2020'):
    """
        The function to create csv file from given url
  
        Parameters: 
            url (str): The url adress to get
            name (str): The name of new csv file
          
        Returns: 
            True if success
    """

    html_text = url_to_file(url, name)
    if html_text == None:
        return False
    r_html = HTML(html=html_text)
    table_class = '.box_mini'
    r_table = r_html.find(table_class)

    if len(r_table) == 0:
        return False

    table_data = []
    header_names = ['currency', 'course', 'change']
    for parsed_table in r_table:
        rows = parsed_table.find("b")
        header_value = [x.text for x in rows]
        table_data.append(header_value)

    df = pd.DataFrame(table_data, columns=header_names)

    os.makedirs(DataFolder, exist_ok=True)
    filepath = os.path.join(DataFolder, f'{name}.csv')
    df.to_csv(filepath, index=False, encoding='utf-8', sep=';')

    return True

# if __name__ == "__main__":
# parse_and_extract(url="https://kursy-walut.mybank.pl/",name="waluty")
