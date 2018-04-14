import datetime
class Model:
    
    def __init__(self):
        self.ids = {}
        fi = open('BlueTeamParty/BlueTeamParty/data/Georeference.csv')
        fi.readline()
        for line in fi:
            spl = line.strip().split(',')
            self.ids[spl[0]] = (float(spl[1]), float(spl[2]))
        fi.close()

    def get_id_lat_lon(self, id):
        return self.ids[id]
        
    def power_prediction_model(self, id):
        latLon = this.get_id_lat_lon(id)

        darkskyJson = darksky.Darksky.forecast(latLon[0], latLon[1])

        params = list(map((lambda x: (datetime.datetime.fromtimestamp(int(x['hourly']['time'])), x['hourly']['temperature'], x['hourly']['cloudCover'])), darkskyJson))
        print(params)