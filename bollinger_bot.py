from pyalgotrade import strategy
from pyalgotrade import plotter
from pyalgotrade.tools import yahoofinance
#from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import bollinger
from pyalgotrade.stratanalyzer import sharpe


import numpy as np
import pprint
import requests
import json as jsn
from pymongo import MongoClient



def get_json(url):
    r = requests.get(url)
    return r.text


def moving_average(x, N):
    #return np.convolve(x, np.ones((N,)) / N)[(N - 1):]
    return np.convolve(x, np.ones((N,)) / N, mode='valid')




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



    #cryptocurrences.insert_many(parced_json)




    #show all database
    #for cryptocurrency in cryptocurrences.find():
    #    pprint.pprint(cryptocurrency)


    running_avg = []

    for cryptocurrency in cryptocurrences.find({u'name': u'Bitcoin'}):
        #pprint.pprint(cryptocurrency)
        #pprint.pprint(float(cryptocurrency[u'price_usd']))
        running_avg.append(float(cryptocurrency[u'price_usd']))

    print(running_avg)

    print(moving_average(running_avg, 3))




if __name__ == "__main__":
    main()