#Goal: insert relevant data into tree table
from functions import *
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/tree_details_species.sql"
table = "tree_details_species"
columns = ["SPECIES","FUNCTIONAL_TYPE"]


transfer_data(input_file, output_file, table,
              columns_to_get=columns)
