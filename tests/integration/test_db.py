from tests.system.base_test import BaseTest,app
from myproject.db import CoinsDb
import pandas as pd

class CoinTest(BaseTest):
    coin = {'data': '2021 - 03 - 10   16: 20:00.246444',
            'asset': 'BTC',
            'free': 0.00309338,
            'locked': 0.00000000,
            'ALL': 0.003093,
            'USDT': 174.301043,
            'BTC': 0.003093,
            'PLN': 669.664609}

    total = {'USDT': 1449,
             'BTC': 0.025,
             'PLN': 3000,
             'data': '2021 - 03 - 10   16: 20:00.246444'}



    def setUp(self):
        self.CurrentDb = CoinsDb('test_db.db')


    def tearDown(self):
        # Database is blank
        with app.app_context():
            self.CurrentDb.drop_table('BTC')
            self.CurrentDb.drop_table('total')

    def test_crud(self):

        with app.app_context():


            coinDf = pd.DataFrame([self.coin])

            self.assertIsNone(self.CurrentDb.get_table_df('BTC'), "Found a table with name 'BTC' before save_to_db")

            self.CurrentDb.add_to_db(csv_dataFrame=coinDf, csv_file_or_table='BTC')
            self.assertIsNotNone(self.CurrentDb.get_table_df('BTC'), "Did not find a table with name 'BTC' after add_to_db")

            self.CurrentDb.drop_table('BTC')
            self.assertIsNone(self.CurrentDb.get_table_df('BTC'), "Found a table with name 'BTC' after drop_table")

    def test_data_json(self):

        coinDf = pd.DataFrame([self.total])
        self.CurrentDb.add_to_db(csv_dataFrame=coinDf, csv_file_or_table='total')
        dataTable=self.CurrentDb.get_json_table(table_name="total")
        self.assertDictEqual(dataTable,self.total, f"The JSON of the table is incorrect. Expected : {self.total}  Received {dataTable}")