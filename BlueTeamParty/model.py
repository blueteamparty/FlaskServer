import datetime
from BlueTeamParty import darksky
import os
import random

class Model:
    
    def __init__(self):
        self.ids = {}

        fi = open('BlueTeamParty/data/Georeference.csv')
        fi.readline()
        for line in fi:
            spl = line.strip().split(',')
            self.ids[spl[0]] = (float(spl[1]), float(spl[2]))
        fi.close()

    def get_id_lat_lon(self, id):
        return self.ids[id]
        
    def power_prediction_model(self, id, curr_state):
        latLon = self.get_id_lat_lon(id)

        darkskyJson = darksky.Darksky.forecast(latLon[0], latLon[1])
        
        params = list(map((lambda x: (datetime.datetime.fromtimestamp(int(x['time'])), x['temperature'], x['cloudCover'])), darkskyJson['hourly']['data']))
        print(params)

        ret = {}
        i = 1
        for param in params:
            ts = param[0].isoformat().replace('T', ' ')
            ret[ts] = {}
            ret[ts]['temperature'] = param[1]
            ret[ts]['cloudCover'] = param[2]
            ret[ts]['availablePower'] = random.randint(0,8)
            ret[ts]['confidenceInterval'] = (0.99 ** i)
            i = i + 1

        return ret