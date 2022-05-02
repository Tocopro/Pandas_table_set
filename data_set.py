import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)

output = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv")
output = output[['company', 'price', ]][output.price == output['price'].max()]
print(output)

output = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv")
car_manufacturers = output.groupby('body-style')
toyota_output = car_manufacturers.get_group('hatchback')
print(toyota_output)

output2 = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv")
result = output2['company'].value_counts()
print(result)


output4 = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv")
car_makers = output4.groupby('company')
price_output = car_makers['company', 'price'].max()
print(price_output)
