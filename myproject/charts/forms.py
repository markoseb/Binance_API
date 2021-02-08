from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class ChartForm(FlaskForm):
    valuesType = SelectField('Choose your value:', choices=[('USDT', 'USDT'), ('PLN', 'PLN'), ('BTC', 'BTC')])
    token = SelectField('Choose your token:', choices=[])
    submit = SubmitField('refresh')
