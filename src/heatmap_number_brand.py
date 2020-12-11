import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt     # for visualisation
import seaborn as sns     # for visualisation
from wordcloud import WordCloud    # for create word cloud
import random    # for use in random color in word cloud

import os
import plotly.express as px
import pycountry

def plot():
    path = '../data/ramen-ratings.csv'
    ramen_data = pd.read_csv(path)
    # Transform the star to number and transform the brand all to lowercase
    ramen_data['Stars'] = pd.to_numeric(ramen_data['Stars'], errors = 'coerce')
    ramen_data['Brand'] = ramen_data['Brand'].str.lower()
    
    
    def transform_country(country_name):
        if country_name == 'Vietnam':
            return 'Viet Nam'
        elif country_name == 'Taiwan':
            return 'Taiwan, Province of China'
        elif country_name == 'USA':
            return 'United States'
        elif country_name == 'South Korea':
            return 'Korea, Republic of'
        elif country_name == 'UK':
            return 'United Kingdom'
        elif country_name == 'Holland':
            return 'Netherlands'
        else:
            return country_name

    ramen_data['Country'] = ramen_data['Country'].map(transform_country)
    # Transform the star to number and transform the brand all to lowercase
    ramen_data['Stars'] = pd.to_numeric(ramen_data['Stars'], errors = 'coerce')
    ramen_data['Brand'] = ramen_data['Brand'].str.lower()
    # Count the amount of brand that got review
    ramen_brand = ramen_data.groupby(['Brand','Country']).agg({'Review #':'count'})
    ramen_brand = ramen_brand.reset_index() 
    ramen_brand = ramen_brand.sort_values('Review #', ascending = False)




    # Count brand from each country that got review
    ramen_coun = ramen_brand.groupby('Country').agg({'Brand':'count'}).reset_index()
    ramen_coun = ramen_coun.rename(columns = {'Brand':'Number_of_Brands_Reviwed'})
    ramen_coun = ramen_coun.sort_values(['Number_of_Brands_Reviwed', 'Country'], ascending = [False, True])

    plt.figure(figsize=(20, 5))
    plt.bar('Country', 'Number_of_Brands_Reviwed', data = ramen_coun, color = 'blue')
    plt.title( 'The amount of ramen brands in each country', fontsize=16)
    plt.ylabel('Number_of_Brands_Reviwed')
    plt.xticks(rotation = 90)
#     plt.show()

    codeToName = {}
    for country in pycountry.countries:
        codeToName[country.alpha_3] = country.name

    def normalize_row(row, data_cache):
        countryName = codeToName[row['iso_alpha']]
        try:
            return list(ramen_coun[ramen_coun['Country'] == countryName].items())[1][1].item()
        except:
            return 0


    
    gapminder = px.data.gapminder().query("year==2007")
    gapminder['Number_of_Brands_Reviwed'] = gapminder.apply(lambda row: normalize_row(row, ramen_coun), axis=1) 

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color='Number_of_Brands_Reviwed', 
                        hover_name="country", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    fig.show()