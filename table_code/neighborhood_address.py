#Goal: insert relevant data into table
from jon_functions import *
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/neighborhood_address.sql"
table = "neighborhood_address"

#parse data
columns = ["Neighborhood", "Address"]
parsed_df = get_parsed_df(input_file, columns)
# drop redundant rows
cleaned_df = parsed_df.drop_duplicates()

#transform data
transform_data(cleaned_df, output_file, table)