import pandas as pd 

a = {"Imię": ["Karmel", "Tofik", "Szary", "Mruczek"], "Wiek": [8,1,0,2], "Rasa kota": ["Mieszany", "Zwykły", "Zwykły", "Zwykły"]}

df = pd.DataFrame(a)
df.columns = ["Imię", "Wiek", "Rasa kota"]
df.index = [1,2,3,4]
print(df)