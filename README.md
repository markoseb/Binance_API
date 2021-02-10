# [Binance API - CHARTS](https://startbootstrap.com/template/simple-sidebar/) -work in progress

##Preview
 
[![Binance API Preview]()]

##Download and Installation

To begin using this template:
*	Download on GitHub
*	create virtual env with all Packages in requirements.txt
*	Add DataFolder in the same directory where Binance_API is located.
*	Enter your own API_KEY & API_SECRET in conf.txt

##Usage

###Basic Usage

After downloading run:
*	set FLASK_APP=app.py
*	flask db init
*	flask db migrate -m "Create first tabels"
*	flask db upgrade
*	python app.

##About

Get data from your Binance account. Check your wallet and make some data science. Using current api version you can:
*	create charts using your binance account data.
*	see your profit for every single coin, or total balance. Compare with previous values.
*	change data type for your charts (USD, BTC,PLN)

##How it works

*	connect with your binance account
*	get your account balance and create database
*	create charts using db
*	set your parameters, refresh your chart

