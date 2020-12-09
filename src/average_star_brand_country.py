import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt     # for visualisation
import seaborn as sns     # for visualisation

ramen_data = pd.read_csv('../data/ramen-ratings.csv')
ramen_data['Stars'] = pd.to_numeric(ramen_data['Stars'], errors = 'coerce')
ramen_data['Brand'] = ramen_data['Brand'].str.lower()



# Group ramen_data by Country and Brand column 
# and calculate the mean and median of Stars that each brand received
ramen_stars = ramen_data.groupby(['Country','Brand']).agg({'Stars': ['mean', 'median'], 'Review #': 'count'})
ramen_stars = ramen_stars.reset_index()
ramen_stars.columns = ['Country','Brand','Mean Stars', 'Median Stars', 'Review#']
ramen_stars = ramen_stars.sort_values('Median Stars', ascending = False)

# Create new column for label
ramen_stars['Country Brand'] = ramen_stars['Brand'] + ' (' + ramen_stars['Country'] + ')'


# View the top 5 brands with the highest average stars (sort by mean)
ramen_stars_re = ramen_stars[ramen_stars['Review#'] >= 10].reset_index()
ramen_stars_re = ramen_stars_re.sort_values('Mean Stars', ascending = False)


# Create box plot with mean
# Sort by median of the stars for the order in box plot
ramen_stars_re = ramen_stars_re.sort_values('Median Stars', ascending = False)

# Create boxplot
ramen_box = ramen_data[['Country','Brand','Stars']].reset_index()
ramen_box['Country Brand'] = ramen_box['Brand'] + ' (' + ramen_box['Country'] + ')'

# Select only brand in country that in ramen_stars_re
ramen_box = ramen_box[ramen_box['Country Brand'].isin(ramen_stars_re['Country Brand'])]

# Create boxplot
fig, ax = plt.subplots(figsize=(5, 20))
sns.boxplot(x = 'Stars', y = 'Country Brand', data = ramen_box, color = 'purple',\
            order = ramen_stars_re['Country Brand'], showmeans = True,\
            meanprops = {'marker': 'o','markerfacecolor': 'saddlebrown', 'markeredgecolor': 'saddlebrown'})
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top') 
plt.title( 'The distribution of the stars in each brand (mean display as brown circles)', \
          fontsize=14)
plt.show()