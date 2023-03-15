import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

# ---------- a ----------

# broj mjerenja
print(len(data))
# tipovi velicina
print(data.head(0))
# postoje li izostale vrijednosti
print(data.isnull().sum())
# postoje li duplicirane vrijednosti
print(data.duplicated())
# brisanje redova gdje barem vrijednost jedne velicine nedosta je
data.dropna(axis=0)
# brisanje dupliciranih redova
data.drop_duplicates()
# konvertiranje kategorickih velicina u tip category
data[data.select_dtypes(['object']).columns] = data.select_dtypes(
    ['object']).apply(lambda x: x.astype('category'))
print(data.dtypes)

# ---------- b ----------

columns = ['Make', 'Model', 'Fuel Consumption City (L/100km)']
new_data = data.sort_values('Fuel Consumption City (L/100km)', ascending=False)[
    ['Make', 'Model', 'Fuel Consumption City (L/100km)']]
# najveca potrosnja
print(new_data.head(3))
# najmanja potrosnja
print(new_data.tail(3))

# ---------- c ----------

new_data = data[data['Engine Size (L)'].between(2.5, 3.5)]
# broj vozila s velicinom motora unutar granica
print(len(new_data))
# prosjecna emisija CO2 tih vozila
print(new_data['CO2 Emissions (g/km)'].mean())

# ---------- d ----------

new_data = data[data['Make'] == 'Audi']
# broj vozila marke Audi
print(len(new_data))
new_data = new_data[new_data['Cylinders'] == 4]
# prosjecna emisija CO2 vozila marke Audi s 4 cilindra
print(new_data['CO2 Emissions (g/km)'].mean())

# ---------- e ----------

print(data['Cylinders'].max())
new_data = data[data["Cylinders"] % 2 == 0]
print(len(new_data['Cylinders']))
for i in new_data['Cylinders'].unique():
    print(new_data[new_data['Cylinders'] == i]['CO2 Emissions (g/km)'].mean())

# ---------- f ----------

diesel_data = data[data['Fuel Type'] == "D"]
gasoline_data = data[(data['Fuel Type'] == "X") | (data['Fuel Type'] == "Z")]
print(diesel_data.loc[:, 'Fuel Consumption City (L/100km)'].mean())
print(gasoline_data.loc[:, 'Fuel Consumption City (L/100km)'].mean())
print(diesel_data.loc[:, 'Fuel Consumption City (L/100km)'].median())
print(gasoline_data.loc[:, 'Fuel Consumption City (L/100km)'].median())

# ---------- g ----------

diesel_4cyl_data = diesel_data[diesel_data['Cylinders'] == 4].sort_values(
    'Fuel Consumption City (L/100km)', ascending=False)
print(diesel_4cyl_data.head(1))

# ---------- h ----------

manual_data = data[data['Transmission'].str.startswith("M")]
print(len(manual_data))

# ---------- i ----------

print(data.corr(numeric_only=True))
