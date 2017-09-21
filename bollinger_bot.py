#from pyalgotrade import strategy
#from pyalgotrade import plotter
#from pyalgotrade.tools import yahoofinance
#from pyalgotrade.barfeed import yahoofeed
#from pyalgotrade.technical import bollinger
#from pyalgotrade.stratanalyzer import sharpe

import time
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
    # https: // api.coinmarketcap.com / v1 / ticker /?limit = 5
    while True:
        print ("This prints once a 5 minutes.")
        #time.sleep(300)


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
            #pprint.pprint(cryptocurrency)




        #for cryptocurrency in cryptocurrences.find({u'name': u'Bitcoin'}):
            #pprint.pprint(cryptocurrency)
            #pprint.pprint(float(cryptocurrency[u'price_usd']))
            #running_avg.append(float(cryptocurrency[u'price_usd']))

        running_avg = []
        for cryptocurrency in cryptocurrences.find({u'name': u'Bitcoin'}).sort("last_updated", -1).limit(3):
            #pprint.pprint(cryptocurrency)
            #pprint.pprint(float(cryptocurrency[u'price_usd']))
            running_avg.append(float(cryptocurrency[u'price_usd']))

        result_to_update = moving_average(running_avg, 3)

        for cryptocurrency in cryptocurrences.find({u'name': u'Bitcoin'}).sort("last_updated", -1).limit(1):
            #result = cryptocurrency.update({{$set: u'rank': float(result_to_update)}})
            result = cryptocurrency.update({'rank': float(result_to_update)})

            result = cryptocurrency.update({'rank': float(result_to_update)})

            #result = cryptocurrency.update({'$set': {'rank': float(result_to_update)}})

            #temp = cryptocurrency.update({u'mov_avg': float(result_to_update)})
            print(result)
            pprint.pprint(cryptocurrency)
            cryptocurrences.save(cryptocurrency)


        #db.users.update({name: "Tom"}, {name: "Tom", age: 25}, {upsert: true})

        for cryptocurrency in cryptocurrences.find():
            pprint.pprint(cryptocurrency)

        #print(moving_average(running_avg, 3))




        time.sleep(3000)



if __name__ == "__main__":
    main()