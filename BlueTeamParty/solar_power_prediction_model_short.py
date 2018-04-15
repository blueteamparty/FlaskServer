import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import datetime


df = pd.read_csv('b9c5abaa-28bd-4c7b-9632-01ca823fb585.csv')
df.shape
df_2 = pd.read_csv('Georeference.csv')
df_3 = pd.read_csv('One_House_2040484054.csv')
df_4 = pd.read_csv('forecast.csv')
df_4['cloudCover'] = df_4['cloudCover'] * 100 # converts cloud cover into percentage

# Normalizing time series for cloud cover and Power generation data
df_3= df_3[df_3.index % 4 == 0]
