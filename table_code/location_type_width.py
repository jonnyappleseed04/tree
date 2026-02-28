#Goal: insert relevant data into table
from jon_functions import *
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/location_type_width.sql"
table = "location_type_width"
columns = ["Site_Width", "Site_Size"]


transfer_data(input_file, output_file, table, columns_to_get=columns)