import newspaper
from time import gmtime, strftime
import pandas as pd

hot_today = newspaper.hot()

hot_date = str(strftime("%Y-%m-%d", gmtime()) + '_hotness.csv')

df = pd.DataFrame(hot_today)

df['rating'] = df.index
df['rank'] = df['rating'].rank(ascending=False)
df = df.drop('rating', axis=1)

df.to_csv(hot_date)