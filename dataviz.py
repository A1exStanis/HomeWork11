# DataViz
# Choose a dataset, you can use Seaborn example datasets. Create a cheat sheet for yourself containing all plot types discussed in the lecture.
# Provide the following info:  
#   - Plot type 
#   - Use cases (categorical data, distribution, etc.) 
#   - Example on the dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
titanic.head()
titanic.describe()

titanic_removed = titanic.dropna()
titanic_removed.isnull()

sns.displot(titanic_removed, x='age')

g = sns.catplot(x="age", y="alive", kind="violin", inner=None, data=titanic_removed)
sns.swarmplot(x="age", y="alive", color="k", size=3, data=titanic_removed, ax=g.ax)

_ = sns.catplot(x="age", y="deck", hue="alive", kind="box", data=titanic_removed)

value = titanic_removed['sex'] == 'male'
titanic_male = titanic_removed[value]

deck_ = titanic_male['deck'] == 'G'
titanic_male[deck_]