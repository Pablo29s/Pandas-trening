import pandas as pd

df = [["Karmel", 8], ["Tofik", 1], ["Szary", 2]]


df = pd.DataFrame(df)
df.columns = ["Imię", "Wiek"]
df["Rasa"] = ["Mieszany", "Zwykły", "Zwykły"]
df["Okres"] = 0

for row in df.itertuples():
    if row.Wiek > 3:
        print(f"Kot {row.Imię} z indexem {row.Index} jest dorosły")
    if row.Wiek < 3:
        print(f"Kot {row.Imię} z indexem {row.Index} jest młody")

