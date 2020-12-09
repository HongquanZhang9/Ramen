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

    codeToName = {}
    for country in pycountry.countries:
        codeToName[country.alpha_3] = country.name
    ramen_data['Country'] = ramen_data['Country'].map(transform_country)
    # Transform the star to number and transform the brand all to lowercase
    ramen_data['Stars'] = pd.to_numeric(ramen_data['Stars'], errors = 'coerce')
    ramen_data['Brand'] = ramen_data['Brand'].str.lower()
    # Count the amount of brand that got review
    
    # Present the variety of each countries that got reviewed
    ramen_variety = ramen_data.groupby(['Country']).agg({'Variety':'count'})
    ramen_variety = ramen_variety.reset_index() 
    ramen_variety = ramen_variety.sort_values(['Variety','Country'], ascending = [False, True])
    ramen_variety = ramen_variety.rename(columns = {'Variety': 'Country variety'})
    
    # Bar chart of the amount of ramen products in each country that got reviewed
    plt.figure(figsize=(15, 5))
    plt.bar('Country', 'Country variety', data = ramen_variety, color = 'peru')
    plt.title( 'The amount of ramen product in each country', fontsize=14)
    plt.ylabel('Number of product')
    plt.xticks(rotation = 90)
    plt.show()

    def normalize_row(row, data_cache):
        countryName = codeToName[row['iso_alpha']]
        try:
            return list(ramen_variety[ramen_coun['Country'] == countryName].items())[1][1].item()
        except:
            return 0
        
    gapminder = px.data.gapminder().query("year==2007")

    

    gapminder['Number_of_Reviews'] = gapminder.apply(lambda row: normalize_row(row, ramen_variety), axis=1) 

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color='Number_of_Reviews', 
                        hover_name="country", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
    fig.show()