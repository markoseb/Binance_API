from myproject import app
from flask import render_template
from myproject.connect import Create_db_graphs_account_balance


# from myproject.sql_data import drop_table,engine
# from sqlalchemy import MetaData

@app.route('/')
def index():
    Create_db_graphs_account_balance()
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
    # metadata = MetaData(engine, reflect=True)
    # drop_table("REEF")
