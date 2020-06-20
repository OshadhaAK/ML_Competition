import googlemaps
import pandas as pd
import numpy as np

API_key = 'API KEY'  # enter Google Maps API key
gmaps = googlemaps.Client(key=API_key)

df = pd.read_csv('test.csv', index_col='tripid')

print(df)

r_list = []
plat = []
plon = []
dlat = []
dlon = []


for row in df.itertuples():
    LatOrigin = row.pick_lat
    LongOrigin = row.pick_lon
    origins = (LatOrigin, LongOrigin)

    LatDest = row.drop_lat
    LongDest = row.drop_lon
    destination = (LatDest, LongDest)

    try:
        plat.append(LatOrigin)
        plon.append(LongOrigin)
        dlat.append(LatDest)
        dlon.append(LongDest)
        result = gmaps.distance_matrix(origins, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
        r_list.append(result)

    except KeyError:

        r_list.append(0)

len(r_list)
d = {'pick_lat': plat, 'pick_lon': plon, 'drop_lat': dlat, 'drop_lon': dlon, 'distance': r_list}
df_new = pd.DataFrame(d)
df_new.to_csv('test_distance_final.csv')

print("ok")
