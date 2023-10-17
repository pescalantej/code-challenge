import pandas as pd

# lista con todos los formatos asociados a valores faltantes
missing_value_formats = ["n.a.","?","NA","n/a", "na", "--","..."]

df = pd.read_csv("empleados.csv", na_values = missing_value_formats)
df = df.dropna(axis=0)

print(df.shape)