from pyalgotrade import strategy
from pyalgotrade import plotter
from pyalgotrade.tools import yahoofinance
#from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import bollinger
from pyalgotrade.stratanalyzer import sharpe



import pprint
import requests
import json as jsn
from pymongo import MongoClient



def get_json(url):
    r = requests.get(url)
    return r.text





def main():
    #https: // api.coinmarketcap.com / v1 / ticker /?limit = 5

    url = "https://api.coinmarketcap.com/v1/ticker/?limit=1"
    json = get_json(url)
    #print(json)


    parced_json = jsn.loads(json)
    #print(parced_json[1])


    client = MongoClient('localhost', 27017)
    db = client.crypto_database
    cryptocurrences = db.cryptocurrences

    cryptocurrences.insert_many(parced_json)

    for cryptocurrency in cryptocurrences.find():
        pprint.pprint(cryptocurrency)





if __name__ == "__main__":
    main()