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

    def ids_as_json(self):
        ret = []
        for key in self.ids:
            temp = [key, str(self.ids[key][0]), str(self.ids[key][1])]
            ret.append(temp)
        return ret
        
    def power_prediction_model(self, id, curr_state):
        latLon = self.get_id_lat_lon(id)

        darkskyJson = darksky.Darksky.forecast(latLon[0], latLon[1])
        
        params = list(map((lambda x: (datetime.datetime.fromtimestamp(int(x['time'])), x['temperature'], x['cloudCover'])), darkskyJson['hourly']['data']))
        print(params)

        ret = []
        i = 1
        for param in params:
            ts = param[0].isoformat().replace('T', ' ')
                  #timestamp, temperature, cloudCover, availablePower, confidenceInterval
            arr = [ts, param[1], param[2], random.randint(0,8), (0.99 ** i)]
            ret.append(arr)
            i = i + 1

        return ret