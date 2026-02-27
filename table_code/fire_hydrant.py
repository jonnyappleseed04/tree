#Goal: create sql file that inserts fire_hydrants in fire_hydrant table
from jon_functions import *
#.. = one level up
input_file = "../csv_files/fire_hydrant.csv"
output_file = "../output_files/fire_hydrant.sql"
table = "fire_hydrant"
# .fillna is to replace "nans" with "nulls"
df = pd.read_csv(input_file).fillna("null")

transform_data(df, output_file, table)
