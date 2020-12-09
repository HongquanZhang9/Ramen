import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt     # for visualisation
import seaborn as sns     # for visualisation

ramen_data = pd.read_csv('./ramen-ratings.csv')
ramen_data['Stars'] = pd.to_numeric(ramen_data['Stars'], errors = 'coerce')
ramen_data['Brand'] = ramen_data['Brand'].str.lower()

# Group ramen_data by Country and Brand column 
# and calculate the mean and median of Stars that each brand received
ramen_stars = ramen_data.groupby(['Country']).agg({'Stars': ['mean', 'median'], 'Review #': 'count'})
ramen_stars = ramen_stars.reset_index()
ramen_stars.columns = ['Country', 'Mean Stars', 'Median Stars', 'Review#']
ramen_stars = ramen_stars.sort_values('Median Stars', ascending = False)

# Group ramen_data by Country and Brand column 
# and calculate the mean and median of Stars that each brand received
ramen_stars = ramen_data.groupby(['Country']).agg({'Stars': ['mean', 'median'], 'Review #': 'count'})
ramen_stars = ramen_stars.reset_index()
ramen_stars.columns = ['Country', 'Mean Stars', 'Median Stars', 'Review#']
ramen_stars = ramen_stars.sort_values('Median Stars', ascending = False)

# Create boxplot
ramen_box = ramen_data[['Country','Stars']].reset_index()
# Select only brand in country that in ramen_stars_re
ramen_box = ramen_box[ramen_box['Country'].isin(ramen_stars['Country'])]


# Create boxplot
fig, ax = plt.subplots(figsize=(10, 15))

sns.boxplot(x = 'Stars', y = 'Country', data = ramen_box, color = 'yellow',\
            order = ramen_stars['Country'], showmeans = True,\
            meanprops = {'marker': 'o','markerfacecolor': 'saddlebrown', 'markeredgecolor': 'saddlebrown'})
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top') 
plt.title( 'The distribution of the stars in each country (mean display as brown circles)', \
          fontsize=15)
plt.show()