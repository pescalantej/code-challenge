import pandas as pd

# list of possible missing values names
missing_value_formats = ["n.a.","?","NA","n/a", "na", "--","..."]

df = pd.read_csv("empleados.csv", na_values = missing_value_formats)

# deleting rows with at least one missing value
df = df.dropna(axis=0)

print(df.shape)