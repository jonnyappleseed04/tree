#Goal: insert relevant data into tree table
from jon_functions import *
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/location_type.sql"
table = "location_type"
columns = ["Site_Type", "Site_Width", "Site_Size", "SITE_IMPROVEMENT", "Wires"]

transfer_data(input_file, output_file, table, columns_to_get=columns,
              auto_increment=True)
