import pandas as pd
import matplotlib.pyplot as plt
import io

def do_plot(country, which):
    if which == "confirmed": 
        df_confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
        drop_coord_df = df_confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
        set_index_to_country = drop_coord_df.set_index('Country/Region')
        new_df = set_index_to_country.transpose()
        new_df.plot(y=country, figsize=(10,5))
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image
    elif which == "deaths":
        df_confirmed = pd.read_csv('time_series_covid19_deaths_global.csv')
        drop_coord_df = df_confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
        set_index_to_country = drop_coord_df.set_index('Country/Region')
        new_df = set_index_to_country.transpose()
        new_df.plot(y=country, figsize=(10,5))
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image