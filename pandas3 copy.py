import pandas as pd 

a = pd.read_csv('Countries-Europe.csv')

df = pd.DataFrame(a)

df["Wielkość_Kraju"] = 0

df['land area km'] = df['land area km'].apply(str) + ' km²'


for row in df.itertuples():
    if row.population > 50000000:
        print(f"{row.Index} Ogromny kraj: {row.name}")
        print("Populacja: ", df.loc[row.Index, "population"])
        print("--------------------------------------------------")
    if row.population > 10000000:
        print(f"{row.Index} Ogromny kraj: {row.name}")
        print("Populacja: ", df.loc[row.Index, "population"])
        print("--------------------------------------------------")
    if row.population > 1000000:
        print(f"{row.Index} Średni kraj: {row.name}")
        print("Populacja: ", df.loc[row.Index, "population"])
        print("--------------------------------------------------")
    if row.population < 1000000:
        print(f"{row.Index} Mały kraj: {row.name}")
        print("Populacja: ", df.loc[row.Index, "population"])
        print("--------------------------------------------------")


    
