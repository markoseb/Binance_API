
import os
import plotly.io._kaleido as pio
from sql_data import get_table_sql
import plotly.express as px
from filePath import DataFolder
#pip3 install termgraph


# Using plotly.express

y_vars=["USDT","BTC","PLN"]
profit = {'profit': 0, 'pr_profit': 0}
def create_plot_img(table_name = ""):
    
    """ 
        The function create plot img from db
  
        Parameters: 
            csv_file_name (str): The table name to read
            
        Returns: 
            
    """
    
    # df = Read_csv(csv_file_name)
    df = get_table_sql(table_name = table_name)
    for y_var in y_vars:
        img_file=table_name+y_var
        get_profit(df, y_var)
        fig = px.line(df, x='data', y=y_var,
                      title=f"{img_file} {profit['profit']} {profit['pr_profit']}% Current Val:{profit['last_val']}",
                      width=2000, height= 800)
        filepath=os.path.join(DataFolder,f'img/{img_file}.png')
        pio.write_image(fig,filepath,format="png",engine="kaleido")

# os.system("termgraph data/TEST.csv")

def get_profit(df, val):

    first_val = df.head(1)[val].values
    last_val = df.tail(1)[val].values
    profit['profit'] = last_val - first_val
    profit['pr_profit'] = profit['profit'] / first_val * 100
    profit['last_val'] = last_val