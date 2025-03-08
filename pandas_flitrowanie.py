import pandas as pd

a = pd.read_csv("car_price_dataset.csv")

df = pd.DataFrame(a)

marki = ["Mercedes", "Honda"]
print("Idealne samochody: ")
print(df[(df["Brand"].isin(marki)) & (df["Price"] > 5000) & (df["Transmission"] == "Manual") & (df["Engine_Size"] > 3)].head(5))