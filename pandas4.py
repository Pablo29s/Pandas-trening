import pandas as pd
import matplotlib.pyplot as plt


cena = input("Cena samochodu (Niska, Wysoka, Średnia, Bardzo niska): \n")
transmission = input("Rodzaj skrzyni biegów (Automatic, Manual, Semi-Automatic): \n")
year = int(input("Rok produkcji (od 2000 do obecnego): \n"))
fuel = input("Rodzaj paliwa (Diesel, Electric, Hybrid, Petrol): \n")




df = pd.read_csv('car_price_dataset.csv')


df["Cena"] = "Nieznana"
df.loc[df["Price"] >= 12000, "Cena"] = "Wysoka"
df.loc[(df["Price"] >= 8500) & (df["Price"] < 12000), "Cena"] = "Średnia"
df.loc[(df["Price"] >= 5500) & (df["Price"] < 8500), "Cena"] = "Niska"
df.loc[df["Price"] < 5500, "Cena"] = "Bardzo niska"


filtered_df = df[(df["Cena"] == cena) & (df["Transmission"] == transmission) & (df["Year"] == year) & (df["Fuel_Type"] == fuel)]


if not filtered_df.empty:
    print("\nIdealne samochody :")
    print(filtered_df[['Brand', 'Model']].to_string(index=False))
else:
    print("\nBrak samochodów spełniających kryteria.")