#Goal: insert relevant data into tree table
from functions import *
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/neighborhood.sql"
table = "neighborhood"
columns = ["Neighborhood"]

transfer_data(input_file, output_file, table, columns_to_get=columns)
