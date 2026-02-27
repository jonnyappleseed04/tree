#Goal: create sql file that inserts fire_hydrants... in fire_hydrant... table
from jon_functions import *
#.. = one level up
input_file = "../csv_files/tree_is_next_to_fire_hydrant.csv"
output_file = "../output_files/tree_is_next_to_fire_hydrant.sql"
table = "tree_is_next_to_fire_hydrant"
df = pd.read_csv(input_file).fillna("null")

transform_data(df, output_file, table)