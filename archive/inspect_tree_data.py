#use to inspect shape of tree_inventory.csv
import pandas as pd

df = pd.read_csv("csv_files/tree_inventory.csv")

print(df.info())

s = df['Y'].astype(str).str.replace('-','', regex=False)

# Maxdigits to the right (Scale)
# We split by the decimal and count the length of the second part
right_digits = s.str.split('.').str[1].fillna('').str.len()
max_scale = right_digits.max_()

# 2. Max total digits (Precision)
# We remove the decimal point and count the length of the remaining string
total_digits = s.str.replace('.', '', regex=False).str.len()
max_precision = total_digits.max_()

print(f"Max digits to the right: {max_scale}")
print(f"Max total digits: {max_precision}")