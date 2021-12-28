import sqlite3
from sqlite3 import Error
import requests
from datetime import datetime


url = 'https://v6.exchangerate-api.com/v6/7fecd5fd0f53bce7359d185f/latest/USD'
print(url)

# Send the request through GET method to read the data
r = requests.get(url=url)

# We will store the response in the object r
print(r)
# Extract the data in json format
data = r.json()
# print(data)

# print(data["conversion_rates"])
rate = data["conversion_rates"]
usd = rate["USD"]
inr = rate["INR"]
ngn = rate["NGN"]
aud = rate["AUD"]
cad = rate["CAD"]
eur = rate["EUR"]
time = str(datetime.now())
print(time)

obj = (time, usd, inr, ngn, aud, cad, eur)


def sql_connector():
    try:
        con = sqlite3.connect('DataBase.db')
        print('Created')
        return con
    except Error:
        print('Error')


con = sql_connector()


def table_create():
    table_data = con.cursor()
    table_data.execute(
        'create table if not exists Data1(time TEXT ,USD real,INR real,NGN real,AUD real,CAD real,EUR real)')


def record_insert(obj):
    table_data = con.cursor()
    # table_data.execute('insert into Data1 values("2021-12-21 14:51:00",1,75,100)')
    table_data.execute(
        'insert into Data1(time,USD,INR,NGN,AUD,CAD,EUR) values(?,?,?,?,?,?,?)', obj)


table_create()
record_insert(obj)


con.commit()
con.close()
