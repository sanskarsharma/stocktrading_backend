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

import collections
@app_instance.route("/live", methods=["POST"])
def live():
   
    ticker = request.form.get("ticker") or "AAPL"
    returntype= request.form.get("returntype") or "json"

    api_response = requests.get(url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+ ticker+"&apikey=WRRV1W3LLQEC5MKX", stream=True)
    raw_data = api_response.text 
    # print(type(rawres)) - str

    my_ordered_dict = json.loads(raw_data, object_pairs_hook=collections.OrderedDict)
    
    resdict = {}

    if "Error Message" in my_ordered_dict:
        resdict["status"] = "0"
        resdict["error"] = "Invalid Request, plese check input"
        resjson = json.dumps(resdict)
        return resjson

    need = my_ordered_dict["Time Series (Daily)"]
    
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
        
        resdict["status"] = "1"
        resdict["data"] = dict
        resjson = json.dumps(resdict)
        return resjson
        
    else:
        c=0
        list =[]
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

    res = {}

    if data is None :
        dict = {}
        dict["error"] = "Invalid Ticker or company data not present in database"
        dict["status"] = "0"
        jso =json.dumps(dict)
        return jso

    datadict = {}
    datadict["id"]= data.id
    datadict["ticker"]= data.ticker
    datadict["name"]= data.name
    datadict["marketcap"]= data.marketcap
    datadict["sector"]= data.sector
    datadict["industry"]= data.industry
    
    res["status"]= "1"
    res["data"] = datadict
    resjson = json.dumps(res)
    print(resjson)
    return resjson

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
    
    res["status"]= "1"
    res["data"] = datadict

    resjson = json.dumps(res)
    print(resjson)
    return resjson


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
