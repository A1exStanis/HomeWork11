# Pandas
#   - Import the dataset from this address and assign it to df variable.
# - Select only the Team, Yellow Cards and Red Cards columns.
# - How many teams participated in the Euro2012?
# - Filter teams that scored more than 6 goals

import pandas as pd

df = pd.read_csv("taskdata.csv")

x = df[['Team','Yellow Cards', 'Red Cards']]

y = df.index.value_counts

q = df[df.Goals>6]