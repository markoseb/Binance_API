import pandas as pd
import logging
import sqlalchemy
import sqlacodegen
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from csv_data import Read_csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from filePath import DataFolder
from sqlalchemy import func, select

engine = create_engine(f"sqlite:///{DataFolder}/crypto_db.db")#mysql,postgres
Base = declarative_base()
metadata = declarative_base()
Seassion= sessionmaker(bind = engine)
my_sess = Seassion()







def csv_to_sql(csv_dataFrame={},csv_file_or_table="CHZ"):

    if len(csv_dataFrame) ==0:
        csv_dataFrame=Read_csv(file_name=f'{csv_file_or_table}')
        csv_dataFrame = csv_dataFrame[["data","asset","free","locked","ALL", "USDT","BTC","PLN"]]

    csv_dataFrame.to_sql(csv_file_or_table,
                    engine,
                    if_exists='append',
                    index = False,
                    dtype={
                             "data": String
                             , "USDT": Float
                             , "BTC": Float
                             , "PLN": Float
                         }

                        )


def get_table_sql(table_name = ""):
    return pd.read_sql_table(table_name, engine)


def drop_table(table_name):

   base = declarative_base()
   metadata = MetaData(engine, reflect=True)
   table = metadata.tables.get(table_name)
   if table is not None:
       logging.info(f'Deleting {table_name} table')
       base.metadata.drop_all(engine, [table], checkfirst=True)



# if __name__ == "__main__":
#     metadata = MetaData(engine, reflect=True)
#     drop_table("LINK")
#     drop_table("DOT")
#     drop_table("BAT")
#     drop_table("ATOM")
#     drop_table("CHZ")
#     drop_table("VITE")





