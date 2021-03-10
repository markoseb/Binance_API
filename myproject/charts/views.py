from flask import Blueprint, render_template, request

from myproject.db import CoinsDb
from myproject.graphs import get_profit, profit
from myproject.charts.forms import ChartForm
charts_blueprints = Blueprint('charts', __name__, template_folder="templates/charts")
coin_list = ["Total_balance"]

CurrentDb=CoinsDb()

@charts_blueprints.route('/charts', methods=['GET', 'POST'])
def add():
    form = ChartForm()

    form.token.choices = [(coin, coin) for coin in coin_list]
    df = CurrentDb.get_table_sql("Total_balance")
    valueType = "USDT"
    get_profit(df, valueType)

    if request.method == 'POST':
        df = CurrentDb.get_table_sql(form.token.data)
        valueType = form.valuesType.data
        if valueType not in df.keys():
            valueType = "USDT"
        get_profit(df, valueType)



    return render_template('lineChart.html', form=form, x_val=df["data"].to_json(), y_val=df[valueType].to_json(),
                           profit=profit)


@charts_blueprints.route('/googlePie', methods=['GET', 'POST'])
def add3dPie():
    graphData=[]
    sampleCoin = ['Task', 'Hours per Day']
    graphData.append(sampleCoin)
    for coin in coin_list:
        df = CurrentDb.get_table_sql(coin)
        get_profit(df, "USDT")
        if coin!="Total_balance":
            sampleCoin = []
            sampleCoin.append(coin)
            sampleCoin.append(profit["last_val"].__float__())
            graphData.append(sampleCoin)
    return render_template('googlePie.html',graphData=graphData )

