import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt     # for visualisation
import seaborn as sns     # for visualisation

ramen_data = pd.read_csv('../data/ramen-ratings.csv')
ramen_data['Stars'] = pd.to_numeric(ramen_data['Stars'], errors = 'coerce')
ramen_data['Brand'] = ramen_data['Brand'].str.lower()

# Group ramen_data by Brand and Brand column 
# and calculate the mean and median of Stars that each brand received
ramen_stars = ramen_data.groupby(['Brand']).agg({'Stars': ['mean', 'median'], 'Review #': 'count'})
ramen_stars = ramen_stars.reset_index()
ramen_stars.columns = ['Brand', 'Mean Stars', 'Median Stars', 'Review#']
ramen_stars = ramen_stars.sort_values('Median Stars', ascending = False)


ramen_stars = ramen_stars[ramen_stars['Review#'] >= 10].reset_index()
ramen_stars = ramen_stars.sort_values('Mean Stars', ascending = False)
ramen_stars = ramen_stars.sort_values('Median Stars', ascending = False)

# Create boxplot
ramen_box = ramen_data[['Brand','Stars']].reset_index()
# Select only brand in Brand that in ramen_stars_re
ramen_box = ramen_box[ramen_box['Brand'].isin(ramen_stars['Brand'])]


# Create boxplot
fig, ax = plt.subplots(figsize=(10, 15))

sns.boxplot(x = 'Stars', y = 'Brand', data = ramen_box, color = 'yellow',\
            order = ramen_stars['Brand'], showmeans = True,\
            meanprops = {'marker': 'o','markerfacecolor': 'saddlebrown', 'markeredgecolor': 'saddlebrown'})
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top') 
plt.title( 'The distribution of the stars in each Brand (mean display as brown circles)', \
          fontsize=15)
plt.show()