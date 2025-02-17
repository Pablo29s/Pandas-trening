import pandas as pd

df = [["Karmel", 8], ["Tofik", 1], ["Szary", 2], ["Mruczek", -1]]


df = pd.DataFrame(df)
df.columns = ["Imię", "Wiek"]
df["Rasa"] = ["Mieszany", "Zwykły", "Zwykły", "Zwykły"]


print("Średnia wieku kotów to: ", df.Wiek.mean())