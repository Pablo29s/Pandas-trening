import pandas as pd

df = pd.read_csv('car_price_dataset.csv')


print(df.groupby(['Year', 'Brand']).size())
