import pandas as pd
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, Float
from myproject.csv_data import Read_csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData,engine
from filePath import DataFolder




class CoinsDb():

    Base = declarative_base()
    metadata = declarative_base()
    myengine=engine
    def __init__(self,dbName="crypto_db.db"):
        self.myengine = create_engine(f"sqlite:///{DataFolder}/{dbName}")  # mysql,postgres
        Seassion = sessionmaker(bind=self.myengine)
        my_sess = Seassion()

    def add_to_db(self, csv_dataFrame={}, csv_file_or_table="CHZ"):

        if len(csv_dataFrame) ==0:
            csv_dataFrame=Read_csv(file_name=f'{csv_file_or_table}')
            csv_dataFrame = csv_dataFrame[["data","asset","free","locked","ALL", "USDT","BTC","PLN"]]

        csv_dataFrame.to_sql(csv_file_or_table,
                    self.myengine,
                    if_exists='append',
                    index = False,
                    dtype={
                             "data": String
                             , "USDT": Float
                             , "BTC": Float
                             , "PLN": Float
                         }

                        )


    def get_table_sql(self,table_name = ""):
        return pd.read_sql_table(table_name, self.myengine)


    def drop_table(self,table_name):

        self.base = declarative_base()
        metadata = MetaData(self.myengine, reflect=True)
        table = metadata.tables.get(table_name)
        if table is not None:
            logging.info(f'Deleting {table_name} table')
            self.base.metadata.drop_all(self.myengine, [table], checkfirst=True)

    def json(csv_dataFrame={}):
        return csv_dataFrame



# if __name__ == "__main__":
#     metadata = MetaData(engine, reflect=True)
#     drop_table("LINK")
#     drop_table("DOT")
#     drop_table("BAT")
#     drop_table("ATOM")
#     drop_table("CHZ")
#     drop_table("VITE")
