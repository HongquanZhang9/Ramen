# Ramen Rating and Analysis

![image-20201209213242108](readmeGraph/hotWords.jpg)

## File Structure

- ### src

  A folder store source code, containing all the .py files. 

- ### data

  A folder store the data used in this project.

- ### figures

  A folder store a .ipynb file which shows all the visualizations we generated in the presentation.
  
- ### readmeGraph

  A folder store graphs presented in the README.md file.


```
.
├── README.md
├── data
│   └── ramen-ratings.csv
├── figures
│   └── figures.ipynb
├── readmeGraph
│   └── hotWords.jpg
├── src
│   ├── __init__.py
│   ├── average_star_brand.py
│   ├── average_star_brand_country.py
│   ├── average_star_country.py
│   ├── continent_size.py
│   ├── dataLoader.py
│   ├── global_and_country_preference.py
│   ├── heatmap_average_rating.py
│   ├── heatmap_number_brand.py
│   ├── heatmap_number_review.py
│   └── ramen_wordcloud.py
└── structure.md

4 directories, 16 files
```


## Run the code

#### There are two methods to run the code.

- ### **Run .ipynb file**

  To see the results (or figures) in the project, visit ***figures/figures.ipynb***, and run each code cell in the ***figures.ipynb*** file. Then the results will show up.

- ### **Run source code**

  If you are interested in the source code and want to see some intermediate results, please visit the **src** folder and run **.py files** by the terminal or IDE you use. For example, you can open  the ***src/dataLoader.py*** file which contains a DataLoader class, free feel to create a DataLoader object and try some methods with the help of the comments.



## Third-Party Modules

- ### pandas

```
pip3 instsall pandas
```

- ### seaborn

```
pip3 instsall seaborn
```

- ### matplotlib

```
pip3 instsall matplotlib
```

- ### wordcloud

```
pip3 instsall wordcloud
```

- ### pycountry

```
pip3 install pycountry
```