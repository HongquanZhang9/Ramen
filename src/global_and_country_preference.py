import matplotlib.pyplot as plt
from src.dataLoader import DataLoader
path = '../data/ramen-ratings.csv'
dataLoader = DataLoader(path)
countries = ['USA', 'China', 'Japan', 'Hong Kong', 'Indonesia', 'Vietnam', 'Thailand', 'Taiwan', 'South Korea', 'Singapore','Malaysia']
countrySeasonings = dataLoader.top5SeasoningsInCountries(countries)
countryFlavour = dataLoader.top5FlavourInCountries(countries)


# top five flavours
topFlavours = {
    'chicken': 325,
    'seafood': 265,
    'beef': 233,
    'pork': 101,
    'mushroom': 48,
}

# top five seasonings
topSeasonings = {
    'spicy': 388,
    'curry': 127,
    'oriental': 57,
    'tonkotsu': 53,
    'thai': 35
}

#top 11 country with the most variety
countryVariety = {
    'Japan': 352,
    'USA': 323,
    'South Korea': 309,
    'Taiwan': 224,
    'Thailand': 191,
    'China': 169,
    'Malaysia': 156,
    'Hong Kong': 137,
    'Indonesia': 126,
    'Singapore': 109,
    'Vietnam': 108,
}

def plotFigures():
    """
    plot figures
    :return: None
    """
    #plot top 11 countries' variety
    name_list = list(countryVariety.keys())
    num_list = list(countryVariety.values())
    plt.barh(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
    plt.title('Top 11 Countries with The Most Varieties')
    plt.xlabel('Count')
    plt.ylabel('Country')
    plt.show()

    #plot the top 5 flavour in global
    name_list = list(topFlavours.keys())
    num_list = list(topFlavours.values())
    plt.barh(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
    plt.title('Global Top Five Flavours')
    plt.xlabel('Count')
    plt.ylabel('Flavour')
    plt.show()

    #plot each country's preference on flavour
    for country in countryFlavour.keys():
        name_list = list(countryFlavour[country].keys())
        num_list = list(countryFlavour[country].values())
        plt.barh(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
        plt.title('Preference of '+ country)
        plt.xlabel('Count')
        plt.ylabel('Flavour')
        plt.show()

    #plot the top 5 seasonings in global
    name_list = list(topSeasonings.keys())
    num_list = list(topSeasonings.values())
    plt.barh(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
    plt.title('Global Top Five Seasonings')
    plt.xlabel('Count')
    plt.ylabel('Seasoning')
    plt.show()

    #plot each country's preference on seasoning
    for country in countrySeasonings.keys():
        name_list = list(countrySeasonings[country].keys())
        num_list = list(countrySeasonings[country].values())
        plt.barh(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
        plt.title('Preference of '+ country)
        plt.xlabel('Count')
        plt.ylabel('Seasoning')
        plt.show()