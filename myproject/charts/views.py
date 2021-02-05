from flask import Blueprint,render_template,request

from myproject.sql_data import get_table_sql
from myproject.charts.forms import ChartForm

charts_blueprints=Blueprint('charts',__name__,template_folder="templates/charts")
coin_list=["Total_balance"]
@charts_blueprints.route('/charts',methods=['GET','POST'])
def add():
    form = ChartForm()

    form.token.choices=[(coin,coin) for coin in coin_list]
    df = get_table_sql("BTC")
    valueType="USDT"

    if request.method == 'POST':
        df = get_table_sql(form.token.data)
        valueType = form.valuesType.data

    return render_template('charts.html',form=form,x_val=df["data"].to_json(),y_val=df[valueType].to_json())


