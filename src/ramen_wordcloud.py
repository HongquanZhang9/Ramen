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

    ramen_sort = ramen_data.sort_values('Stars').dropna(subset = ['Stars'])
    ramen_top = ramen_sort.head(500)
    ramen_bottom = ramen_sort.tail(100)
    ramen_top_str = ramen_top['Variety'].str.cat(sep=',')

    # For generate color
    def orange_color_func(word, font_size, position, orientation, random_state=None,\
                        **kwargs):
        return "hsl(%d, 80%%, 60%%)" % random.randint(25, 90)

    # Plot word cloud of the top 100
    stopword_list = ['Noodle', 'Noodles', 'Instant', 'Ramen', 'With']
    plt.figure(figsize=(10,6))
    top_wordcloud = WordCloud(max_font_size= 50, background_color='white', \
                        prefer_horizontal = 0.7, stopwords = stopword_list).generate(ramen_top_str)
    plt.imshow(top_wordcloud.recolor(color_func = orange_color_func, random_state = 3), interpolation='bilinear')
    plt.axis('off')
    plt.show()