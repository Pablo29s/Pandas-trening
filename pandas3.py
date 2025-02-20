import pandas as pd
import matplotlib.pyplot as plt

a = [["Karmel", 8], ["Tofik", 1], ["Szary", 2]]
b = {"Imię": ["Biało-czarny", "Karmelczyk", "Mruczek"], "Wiek": [3, 2, 5], "Rasa": ["Rasowy", "Mieszany", "Zwykły"]}

df1 = pd.DataFrame(a)
df2 = pd.DataFrame(b)

print(df1.plot(kind='bar'))
