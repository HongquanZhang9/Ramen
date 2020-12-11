import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def plot():
    ramen = pd.read_csv('../data/ramen-ratings.csv')

    dic = {'Australia':'Australia',
    'Bangladesh'	:	'Asia',
    'Brazil'	:	'South America',
    'Cambodia'	:	'Asia',
    'Canada'	:	'North America',
    'China'	:	'Asia',
    'Colombia'	:	'South America',
    'Dubai'	:	'Asia',
    'Estonia'	:	'Europe',
    'Fiji'	:	'Australia',
    'Finland'	:	'Europe',
    'Germany'	:	'Europe',
    'Ghana'	:	'Africa',
    'Holland'	:	'Europe',
    'Hong Kong'	:	'Asia',
    'Hungary'	:	'Europe',
    'India'	:	'Asia',
    'Indonesia'	:	'Asia',
    'Japan'	:	'Asia',
    'Malaysia'	:	'Asia',
    'Mexico'	:	'North America',
    'Myanmar'	:	'Asia',
    'Nepal'	:	'Asia',
    'Netherlands'	:	'Europe',
    'Nigeria'	:	'Africa',
    'Pakistan'	:	'Asia',
    'Philippines'	:	'Asia',
    'Poland'	:	'Europe',
    'Sarawak'	:	'Asia',
    'Singapore'	:	'Asia',
    'South Korea'	:	'Asia',
    'Sweden'	:	'Europe',
    'Taiwan'	:	'Asia',
    'Thailand'	:	'Asia',
    'UK'	:	'Europe',
    'United States'	:	'North America',
    'USA'	:	'North America',
    'Vietnam'	:	'Asia'}
    ramen.drop(ramen.loc[ramen['Stars']=='Unrated'].index, inplace=True)
    ramen.reset_index(drop=True, inplace=True)
    #ramen['Stars'] = ramen['Stars'].astype(float)
    for i in range(len(ramen)):
    #     print(ramen.loc[i, 'Country'])
        ramen.loc[i, 'Country'] = dic[ramen.loc[i, 'Country']]
    table = ramen.pivot_table(columns = 'Style', index = "Country",values = "Review #", aggfunc=len, margins=True, dropna=True, fill_value=0)
    table2 = table.div(len(ramen), axis=0).astype('float')
    f = lambda x: '%.2f' % x
    table2 = table2.applymap(f)
    table2 = table2.astype('float64')
    table3 = table2.loc[table2['All']>0.00]
    table3.drop(['Bar', 'Box', 'Can'], axis=1, inplace=True)
    fig, ax = plt.subplots(figsize=(11, 9))
    sb.heatmap(table3, annot = True)
    plt.title('Heat Map of reviews percentage')
    plt.ylabel('Continent')
    plt.show()

    ramen['Stars'] = ramen['Stars'].astype(float)
    table = ramen.pivot_table(columns = 'Style', index = "Country",values = "Stars", dropna=True, fill_value=0,margins = True)

    fig, ax = plt.subplots(figsize=(11, 9))
    sb.heatmap(table, annot = True)
    plt.title('Heat Map of rates')
    plt.ylabel("continent")
    plt.show()


