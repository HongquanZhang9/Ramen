import pandas as pd
class DataLoader:
    """
    Data Loader
    """
    flavours = {
        'beef': 0,
        'chicken': 0,
        'mushroom': 0,
        'laksa': 0,
        'crab': 0,
        'chilli': 0,
        'pepper': 0,
        'tom yam': 0,
        'seafood': 0,
        'spicy': 0,
        'curry': 0,
        'kyushu white': 0,
        'thai': 0,
        'china': 0,
        'japan': 0,
        'tokyo': 0,
        'cream': 0,
        'sriacha': 0,
        'lime': 0,
        'hot': 0,
        'shrimp': 0,
        'tonkotsu': 0,
        'pork': 0,
        'lamb': 0,
        'oriental': 0,
        'tomato': 0,
        'sour':0
    }
    def __init__(self, filePath):
        """
        init and filter invalid data
        :param filePath: the path of the csv file
        """
        self.filePath = filePath
        self.data = pd.read_csv(filePath)
        self.data['Stars'] = self.data['Stars'].apply(lambda x: 0 if x=='Unrated' else float(x))

    def topReviewForEachItem(self):
        res = self.data.sort_values(by='Review #', ascending=False)
        return res

    def topReviewForEachBrand(self):
        """
        Top brands with the most popular ramens sorted by the number of review
        :return: DataFrame
        """
        res = self.data.groupby('Brand').agg({'Review #': 'sum'}).sort_values(by='Review #', ascending=False)
        return res

    def topStarForEachItem(self):
        """
        Top items sorted by stars
        :return: DataFrame
        """
        res = self.data.sort_values(by='Stars', ascending=False)
        return res


    def topMeanStarsForEachBrand(self):
        """
        Top brands with the most popular ramens sorted by mean of stars
        :return: DataFrame
        """
        res = self.data.groupby('Brand').agg({'Stars': 'mean'}).sort_values(by='Stars', ascending=False)
        return res

    def topCountryForMeanStars(self):
        """
        Top countries with the most popular ramens sorted by mean of stars
        :return: DataFrame
        """
        res = self.data.groupby('Country').agg({'Stars': 'mean'}).sort_values(by='Stars', ascending=False)
        return res

    def groupCountry(self):
        res = self.data.groupby('Country').count()
        return res

    def styleInCountry(self):
        """
        Record the number of each style consumed in each country
        dic[country][style] = a number
        :return: a dictionary
        """
        dic = {}
        for index, row in self.data.iterrows():
            if row['Country'] not in dic:
                dic[row['Country']] = {}
            else:
                dic[row['Country']][row['Style']] = dic[row['Country']].setdefault(row['Style'],0)+1
        return dic

    def topStyleInCountry(self):
        """
        The most popular styles in each country
        :return: a dictionary
        """
        dic = self.styleInCountry()
        res = {}
        for country, styles in dic.items():
            theMax = 0
            res[country] = []
            for style, number in styles.items():
                if number==theMax:
                    res[country].append((style,number))
                elif number>theMax:
                    theMax = number
                    res[country].clear()
                    res[country].append((style, number))
        return res

    def countFlavour(self, brand=None, country=None):
        """
        count the number of each similar flavour
        :param brand: default is None, meaning count all the brands in.
        It can receive a brand (string) to specify a brand
        :param country: default is None, meaning count all the countries in.
        It can receive a country (string) to specify a country
        :return: dictionary
        """

        flavours = dict(DataLoader.flavours)
        for index, row in self.data.iterrows():
            if brand:
                if row['Brand'] != brand:
                    continue
            if country:
                if row['Country'] != country:
                    continue
            words = row['Variety'].split()
            for word in words:
                if word.lower() in flavours:
                    flavours[word.lower()]+=1
        return flavours

    def topFlavourInEachCountry(self, brand = None):
        """
        find top flavour in each country, filtered by brand
        :param brand: default is None, it can specify a brand
        :return: dic
        """
        flavours = dict(DataLoader.flavours)
        dic = {}
        for index, row in self.data.iterrows():
            if brand:
                if row['Brand'] != brand:
                    continue
            country = row['Country']
            if country not in dic:
                dic[country] = dict(flavours)
            words = row['Variety'].split()
            for word in words:
                if word.lower() in flavours:
                    dic[country][word.lower()]+=1
        res = {}
        for country, fla in dic.items():
            count = 0
            temp = []
            for k, v in fla.items():
                if v>count:
                    temp.clear()
                    temp.append((k, v))
                    count = v
                elif v==count and v!=0:
                    temp.append((k,v))
            if temp:
                res[country] = list(temp)

        return res

    def topFlavourInEachBrand(self, country = None):
        """
        find top flavour in each brand, filtered by country
        :param country: default is None, it can specify a country
        :return: dic
        """
        flavours = dict(DataLoader.flavours)
        dic = {}
        for index, row in self.data.iterrows():
            if country:
                if row['Country'] != country:
                    continue
            brand = row['Brand']
            if brand not in dic:
                dic[brand] = dict(flavours)
            words = row['Variety'].split()
            for word in words:
                if word.lower() in flavours:
                    dic[brand][word.lower()]+=1
        res = {}
        for brand, fla in dic.items():
            count = 0
            temp = []
            for k, v in fla.items():
                if v>count:
                    temp.clear()
                    temp.append((k, v))
                    count = v
                elif v==count and v!=0:
                    temp.append((k,v))
            if temp:
                res[brand] = list(temp)

        return res

    def top5FlavourInCountries(self, countries):
        res = {}
        for country in countries:
            dic = self.countFlavour(country = country)
            flavourDic = {
                'chicken': 0,
                'seafood': 0,
                'beef': 0,
                'pork': 0,
                'mushroom': 0,
            }
            for k, v in dic.items():
                if k == 'seafood' or k == 'crab' or k == 'shrimp':
                    flavourDic['seafood']+=v
                elif k in flavourDic:
                    flavourDic[k]+=v
            res[country] = dict(flavourDic)
        return res

    def top5SeasoningsInCountries(self, countries):
        res = {}
        for country in countries:
            dic = self.countFlavour(country = country)
            topSeasonings = {
                'spicy': 0,
                'curry': 0,
                'oriental': 0,
                'tonkotsu': 0,
                'thai': 0
            }
            for k, v in dic.items():
                if k == 'spicy' or k == 'hot':
                    topSeasonings['spicy']+=v
                elif k in topSeasonings:
                    topSeasonings[k]+=v
            res[country] = dict(topSeasonings)
        return res

# path = '../data/ramen-ratings.csv'
# dataLoader = DataLoader(path)
# countries = ['USA', 'China', 'Japan', 'Hong Kong', 'Indonesia', 'Vietnam', 'Thailand', 'Taiwan', 'South Korea', 'Singapore','Malaysia']
# print(dataLoader.top5SeasoningsInCountries(countries))