import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import randomized_svd

movies = pd.read_csv('movie/movies.csv')


df = pd.read_csv('movie/ratings.csv')


df = pd.merge(df,movies,on='movieId')

# print(df.head(20))

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())



ratings['no_of_ratings'] = df.groupby('title')['rating'].count()

# print(ratings[ratings['no_of_ratings'] > 100].sort_values(by='no_of_ratings',ascending=False))

# ratings['no_of_ratings'].plot.hist(bins=100)

# ratings['rating'].plot.hist(bins=50)

# sns.jointplot(data=ratings,x='rating',y='no_of_ratings')


# plt.show()

moviemat = df.pivot_table(index='userId',values='rating',columns='title')

# print(moviemat)

ratings = ratings.sort_values(by='no_of_ratings',ascending=False)

shawshank_redemption_ratings = moviemat['Shawshank Redemption, The (1994)']

# print(shawshank_redemption_ratings)

forrest_gump_ratings = moviemat['Forrest Gump (1994)']

# print(forrest_gump_ratings)

forrest_gump_similar = moviemat.corrwith(forrest_gump_ratings).sort_values(ascending=False)

shawshank_redemption_similar = moviemat.corrwith(shawshank_redemption_ratings).sort_values(ascending=False)

corr_shawshank = pd.DataFrame(shawshank_redemption_similar,columns=['corr_shawshank'])

# print(corr_shawshank)

corr_shawshank = corr_shawshank.join(ratings['no_of_ratings'])

# print(corr_shawshank.sort_values('no_of_ratings',ascending=False)[50:60])

corr_shawshank = corr_shawshank[corr_shawshank['no_of_ratings']>60].sort_values('corr_shawshank',ascending=False)

# print(corr_shawshank)

corr_forestgump = pd.DataFrame(forrest_gump_similar,columns=['corr_forest']).join(ratings['no_of_ratings'])
# print(moviemat)
# print(forrest_gump_similar)

corr_forestgump = corr_forestgump[corr_forestgump['no_of_ratings'] > 60].sort_values(by='corr_forest',ascending=False)

print(corr_forestgump)

corr_pulpfiction = pd.DataFrame(moviemat.corrwith(moviemat['Pulp Fiction (1994)']),columns=['corr_pulp']).join(ratings['no_of_ratings'])

corr_pulpfiction = corr_pulpfiction.loc[(corr_pulpfiction['no_of_ratings'] > 60) & (corr_pulpfiction['corr_pulp'] > 0.3)].sort_values(by='corr_pulp',ascending=False)

print(corr_pulpfiction)
