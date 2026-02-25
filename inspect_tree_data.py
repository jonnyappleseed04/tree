#use to inspect shape of tree_inventory.csv
import pandas as pd

df = pd.read_csv("csv_files/tree_inventory.csv")

print(df.info())