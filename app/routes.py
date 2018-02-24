from app import app_instance, db_instance
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, NotificationForm
from flask import request

from datetime import datetime
import time
from pyfcm import FCMNotification
import random
from faker import Faker

import json


@app_instance.route("/home")
@app_instance.route("/")
def home():
    user = {'username': 'sample'}
    return render_template('home.html', title='Home', user=user)
  


from app.models import Companyinfo, Histo
import requests
from app.classes import Prices

    
@app_instance.route("/testing")
def test():
    res = Histo.query.filter_by(symbol="AAPL")
    return str(res[0].id)

@app_instance.route("/live", methods=["POST"])
def live():
    # res = Histo.query.filter_by(symbol="AAPL")
    # return str(res[0].id)
    ticker = request.form.get("ticker") or "AAPL"
    returntype= request.form.get("returntype") or "json"

    api = requests.get(url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+ ticker+"&apikey=WRRV1W3LLQEC5MKX")
    json_data = api.json()
    need = json_data["Time Series (Daily)"]
    #n = need["2018-01-09"]
    #print(type(n))
    list = []

    c=0
    if( returntype == "json"):
        datelist =[]
        openlist = []
        highlist= []
        lowlist= []
        closelist =[]
        adjcloselist= []
        volumelist= []
        dividendamtlist = []
        splitcoefflist=[]
        for date, data in need.items():
            datelist.append(date)
            openlist.append(float(data["1. open"]))
            highlist.append(float(data["2. high"]))
            lowlist.append(float(data["3. low"]))
            closelist.append(float(data["4. close"]))
            adjcloselist.append(float(data["5. adjusted close"]))
            volumelist.append(float(data["6. volume"]))
            dividendamtlist.append(float(data["7. dividend amount"]))
            splitcoefflist.append(float(data["8. split coefficient"]))

        dict = {}
        dict["date"] = datelist
        dict["open"] = openlist
        dict["high"] = highlist
        dict["low"] = lowlist
        dict["close"] = closelist
        dict["adjclose"] = adjcloselist
        dict["volume"] = volumelist
        dict["dividend"] = dividendamtlist
        dict["splitcoeff"] = splitcoefflist

        datajson = json.dumps(dict)
        print datajson
        return datajson
        
        
        
        
            

    else:
        for m, n in need.items():
            c = c+1
            obj = Prices()      # add more fileds to class Prices and frontend left
            obj.date =  m
            obj.open = n["1. open"]
            obj.high = n["2. high"]
            obj.low = n["3. low"]
            obj.close = n["4. close"]
            list.append(m)    
    return str(need) #render_template("market_analysis.html", list = list)


@app_instance.route("/stockinfo",methods=["POST"])
def stockinfo():

    ticker = request.form.get("ticker") or "MSFT"

    data = Companyinfo.query.filter_by(ticker=ticker).first()

    datadict = {}
    datadict["id"]= data.id
    datadict["ticker"]= data.ticker
    datadict["name"]= data.name
    datadict["marketcap"]= data.marketcap
    datadict["sector"]= data.sector
    datadict["industry"]= data.industry
    
    datajson = json.dumps(datadict)
    print(datajson)
    return datajson

@app_instance.route("/stockinfo/<ticker>",methods=["GET"])
def stockinfotick(ticker):
    data = Companyinfo.query.filter_by(ticker=ticker).first()

    datadict = {}
    datadict["id"]= data.id
    datadict["ticker"]= data.ticker
    datadict["name"]= data.name
    datadict["marketcap"]= data.marketcap
    datadict["sector"]= data.sector
    datadict["industry"]= data.industry
    
    datajson = json.dumps(datadict)
    print(datajson)
    return datajson


@app_instance.route("/stockinfo/<ticker>/<field>",methods=["GET"])
def stockinforest(ticker,field):


    data = Companyinfo.query.filter_by(ticker=ticker).first()

    datadict = {}
    datadict["id"]= data.id
    datadict["ticker"]= data.ticker
    datadict["name"]= data.name
    datadict["marketcap"]= data.marketcap
    datadict["sector"]= data.sector
    datadict["industry"]= data.industry
    
    datajson = json.dumps(datadict)
    print(datajson)

    if field==None:
        return datajson
    else:
        if data is not None:
            return datadict[field]



@app_instance.route("/bestperforming")
def bestperforming():
    return "besht"
