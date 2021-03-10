from binance.client import Client
from filePath import API_KEY, API_SECRET, DataFolder
import datetime
from myproject import csv_data, scrape
import os
import pandas as pd
from myproject.charts.views import coin_list, CurrentDb

client = Client(API_KEY, API_SECRET)

endpoint = "https://api.binance.com"
endpoint_path = "/sapi/v1/capital/config/getall"

BTCUSDT = client.get_symbol_ticker(symbol="BTCUSDT")

header_names = ["data"]

total_headers = ["data", "USDT", "BTC", "PLN"]
data_time = datetime.datetime.now()


def Create_db_graphs_account_balance():
    """
    The function to read Binance account balance
    and create csv and png files (graphs)

    """

    account_inf = client.get_account()
    account_balance = account_inf["balances"]
    total_coins_balance = {"USDT": 0.0, "BTC": 0.0, "PLN": 0.0}
    if len(account_balance) > 0:  # nie potrzebne
        scrape.parse_and_extract(url="https://kursy-walut.mybank.pl/", name="Exchange_rates")

        for coin in account_balance:

            if float(coin["free"]) > 0 or float(coin["locked"]) > 0:

                Expand_coin_dictionary(coin=coin)

                Get_headers_names(coin=coin)

                if float(coin["USDT"]) > 1:
                    if not(any(elem in coin["asset"] for elem in coin_list)):
                        coin_list.append(coin["asset"])
                    data = {"data": data_time}

                    Get_total_coins_balance(total_coins_balance,coin=coin, data=data)

                    Create_db_img(coin=coin, data=data)

        dataFramee = pd.DataFrame([total_coins_balance])
        CurrentDb.add_to_db(dataFramee, "Total_balance")
        # create_plot_img("Total_balance")


def Add_item_coin_value(price_units="", coin={}):
    """
    The function to add new item to coin dictonary
    This function allows to add total coin price in new unit
        Parameters: 
        price_units (str): The name of new item. New total price unit
        coin (dict): coin dictonary
          
    Returns: 
        True if success
    """

    if coin["asset"] == "USDT" and price_units == "BTC":
        coin[price_units] = float(coin["USDT"]) / float(BTCUSDT["price"])
        return True

    if coin["asset"] != price_units:
        my_symbol = coin["asset"] + price_units
        price = client.get_symbol_ticker(symbol=my_symbol)
        coin[price_units] = Get_coin_value(coin["ALL"], price['price'])
        return True
    else:
        coin[price_units] = coin["ALL"]
        return False


def Expand_coin_dictionary(coin={}):
    coin["ALL"] = float(coin["free"]) + float(coin["locked"])
    Add_item_coin_value(price_units="USDT", coin=coin)
    Add_item_coin_value(price_units="BTC", coin=coin)

    coin["PLN"] = Get_coin_value(coin["USDT"], csv_data.Read_course_from_csv())
    # coin["USDT-BTC"]=Get_coin_value(coin["BTC"],BTCUSDT["price"])
    # coin["BTC(<-USDT)"]= float(coin["USDT"])/ float(BTCUSDT["price"])


def Get_headers_names(coin={}):
    if len(header_names) == 1:
        for key in list(coin.keys()):
            header_names.append(key)


def Get_total_coins_balance(total_coins_balance,coin={}, data={}):
    for total_key in total_headers:
        if total_key == "data":
            total_coins_balance["data"] = data["data"]
        else:
            total_coins_balance[total_key] = total_coins_balance[total_key] + float(coin[total_key])


def Create_db_img(coin={}, data={}):
    available_coin_list = []
    filepath = os.path.join(DataFolder, f'{coin["asset"]}.csv')
    data.update(coin)
    # available_coin_list.append(data)
    # csv_data.Write_csv_file(data_list= available_coin_list,columns=header_names,filepath=filepath)
    dataFramee = pd.DataFrame([data])
    CurrentDb.add_to_db(dataFramee, coin['asset'])
    # create_plot_img(coin["asset"])


def Get_coin_value(number="", price=""):
    """
        The function to Get total coin value
  
        Parameters: 
            number (str): The total coin number
            price (str): The current rate
          
        Returns: 
            New total price  (float)  
    """
    if len(price) > 0:
        n = float(number)
        p = float(price)
        return n * p
    else:
        return number

#
# if __name__ == "__main__":
#     Create_db_graphs_account_balance()
