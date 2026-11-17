import helperfunctions.data as data

filename = 'datasets/bakery_sales_dataset.csv'
df = data.load_csv(filename)

df.info()
print(df.head())