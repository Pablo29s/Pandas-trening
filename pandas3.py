import pandas as pd 

a = pd.read_csv('Countries-Europe.csv')

df = pd.DataFrame(a)

df["Wielkość_Kraju"] = 0

df['land area km'] = df['land area km'].apply(str) + ' km²'


for index, row in df.iterrows():
    if row['population'] > 50000000:
        df.loc[index, 'Wielkość_Kraju'] = 'Ogromne'
    elif row['population'] > 10000000:
        df.loc[index, 'Wielkość_Kraju'] = 'Duże'
    elif row['population'] > 1000000:
        df.loc[index, 'Wielkość_Kraju'] = 'Średnie'
    elif row['population'] < 1000000:
        df.loc[index, 'Wielkość_Kraju'] = 'Małe'

df['population'] = ((df['population'] / 1000000).round(2)).apply(str) + ' mln'
print(df[df['Wielkość_Kraju'] == 'Małe'])


