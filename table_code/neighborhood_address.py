#Goal: insert relevant data into table
from jon_functions import *
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/neighborhood_address.sql"
table = "neighborhood_address"
columns = ["Neighborhood", "Address"]

transfer_data(input_file, output_file, table, columns_to_get=columns)