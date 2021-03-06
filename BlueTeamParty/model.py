import datetime
from BlueTeamParty import darksky
#from BlueTeamParty import solar_power_prediction_model
import os
import random
import time

#import numpy as np
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#from sklearn.model_selection import KFold
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.decomposition import PCA
#from sklearn.model_selection import train_test_split

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
            powerInBattery = curr_state + self.predict_pv_power(id, param[2]) - self.predict_home_usage(id, param[1], param[0].hour)
            availablePower = powerInBattery - 2 # 2 kWh from a 10 kWh battery, for reserve
            #timestamp, temperature, cloudCover, availablePower, confidenceInterval, powerInBattery
            arr = [ts, param[1], param[2], availablePower, (0.99 ** i), powerInBattery]
            ret.append(arr)
            i = i + 1

        return ret

    # Take cloudcover prediction and site id, load from config site model params via site id
    # then generate power production prediction for site during hour
    def predict_pv_power(self, id, cloudcover):
        site_params = self.get_site_config_vars(id)

        # Stub for model using site parameters, replace this with ML regression model for PV prediction
        predicted_power = site_params[0] * site_params[1] * cloudcover

        # Actual regression created model for solar PV power prediction based on dark sky cloud cover
        #df = pd.read_csv('b9c5abaa-28bd-4c7b-9632-01ca823fb585.csv')
        #df.shape
        #df_2 = pd.read_csv('Georeference.csv')
        #df_3 = pd.read_csv('One_House_2040484054.csv')
        #df_4 = pd.read_csv('forecast.csv')

        #df_test = pd.read_csv('test.csv')
        #df_test.head()
        #df_test['cloudCover'] = df_test['cloudCover']*100

        # Normalizing time series for cloud cover and Power generation data
        #predicted_power = df_3[df_3.index % 4 == 0]

        return predicted_power

    # Take temperature prediction and site id, load from config site model params via site id
    # then generate home power consumption prediction for site during hour
    def predict_home_usage(self, id, temperature, hour_of_day):
        site_params = self.get_site_config_vars(id)

        # Stub for model using site parameters, replace this with ML regression model for home
        # power consumption, assuming households can be broken into a few basic energy demand
        # models, and characterized by an offset % from that model
        predicted_power_consumption = self.get_usage_function(site_params[2])(hour_of_day,temperature) * site_params[3]

        return predicted_power_consumption


    # Take site id, return model offset % for site and system size offset for site
    def get_site_config_vars(self, id):
        # Per site: (id,
        #            % offset from base model,
        #            system size multiplier for model - kW,
        #            usage category type - 1:10, usage modifier %)
        site_vars = {
            str(2040484054): (.9, 10, 3, .8),
            str(1004898253): (.95, 7, 7, .8)
            }

        return site_vars[str(id)]

    def get_usage_function(self, usage_type):
        usage_types = {
            str(0): self.usage_function_0,
            str(1): self.usage_function_1,
            str(2): self.usage_function_2,
            str(3): self.usage_function_3,
            str(4): self.usage_function_4,
            str(5): self.usage_function_5,
            str(6): self.usage_function_6,
            str(7): self.usage_function_7,
            str(8): self.usage_function_8,
            str(9): self.usage_function_9
            }
        return usage_types[str(usage_type)]

    def usage_function_0(self, time_of_day, temperature):
        return time_of_day * temperature * 2

    def usage_function_1(self,time_of_day, temperature):
        return time_of_day * temperature * 2

    def usage_function_2(self, time_of_day, temperature):
        return time_of_day * temperature * 2
    def usage_function_3(self, time_of_day, temperature):
        return time_of_day * temperature * 2
    def usage_function_4(self, time_of_day, temperature):
        return time_of_day * temperature * 2
    def usage_function_5(self, time_of_day, temperature):
        return time_of_day * temperature * 2
    def usage_function_6(self, time_of_day, temperature):
        return time_of_day * temperature * 2
    def usage_function_7(self, time_of_day, temperature):
        return time_of_day * temperature * 2
    def usage_function_8(self, time_of_day, temperature):
        return time_of_day * temperature * 2
    def usage_function_9(self, time_of_day, temperature):
        return time_of_day * temperature * 2
