from unittest import TestCase
from unittest.mock import patch


class UnitConnect(TestCase):
    import myproject.connect as con

    data = {"data": con.data_time}

    total = {'USDT': 0,
             'BTC': 0,
             'PLN': 0,
             'data': ''}

    coin1 = {'data': data['data'],
            'asset': 'BTC',
            'free': 1,
            'locked': 0.00000000,
            'ALL': 1,
            'USDT': 170,
            'BTC': 0.003,
            'PLN': 700}

    coin2 = {'data': data['data'],
            'asset': 'ETC',
            'free': 2,
            'locked': 0.00000000,
            'ALL': 2,
            'USDT': 100,
            'BTC': 0.002,
            'PLN': 500}

    coinNoData = {'asset': 'ETC',
            'free': 2,
            'locked': 0.00000000,
            'ALL': 2,
            'USDT': 100,
            'BTC': 0.002,
            'PLN': 500}


    # use once in the beggining of run test.
    #delate classmethod if you want use setUp befor every single method
    @classmethod
    def setUp(self):
        self.n = "2.0"
        self.p = "5.0"
        self.empty= ""
    def tearDown(self):
        pass
    def test_get_coin_value(self):
        self.assertTrue(self.con.Get_coin_value(self.n,self.p)==10)
        self.assertTrue(self.con.Get_coin_value(self.n, self.empty) == self.n)

    def test_Get_headers_names(self):
        self.con.Get_headers_names(coin=self.coin1)
        expected=["data","asset","free","locked","ALL","USDT","BTC","PLN"]
        self.assertEqual(self.con.header_names,expected)

    def test_Get_total_coins_balance(self):

        expected = {'USDT': 270,
             'BTC': 0.005,
             'PLN': 1200,
             'data': self.data['data']}

        self.con.Get_total_coins_balance(self.total,self.coin1,self.data)
        self.con.Get_total_coins_balance(self.total, self.coin2, self.data)

        self.assertDictEqual(self.total, expected,f'Wrong total coins var. {self.total} != {expected}')

    def test_Add_item_coin_value(self):
        coin = {'data': self.data['data'],
                'asset': 'BTC',
                'free': 1,
                'locked': 0.00000000,
                'ALL': 1,
                'BTC': 0.003,
                'PLN': 700}
        self.assertTrue(self.con.Add_item_coin_value('USDT',coin))

