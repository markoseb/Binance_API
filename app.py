from myproject import app
from flask import render_template,jsonify #flask return string if you want dict use jsonify
from myproject.connect import Create_db_graphs_account_balance


# from myproject.db import drop_table,engine,get_table_sql
# from sqlalchemy import MetaData

@app.route('/')
def home():
    Create_db_graphs_account_balance()
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
    # metadata = MetaData(engine, reflect=True)
    # drop_table("ETH")
    # print (metadata.tables.keys())
