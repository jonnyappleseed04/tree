#Goal: insert relevant data into tree table
from jon_functions import *
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/tree.sql"
table = "tree"
columns = ["OBJECTID","Date_Inventoried","X","Y"]

#note: don't know why getting rid of duplicate rows reduces it so much
transfer_data(input_file, output_file, table,
              columns_to_get=columns)