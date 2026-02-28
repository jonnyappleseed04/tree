#Goal: insert relevant data into tree table
from jon_functions import *
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/neighborhood.sql"
table = "neighborhood"
#parse data
columns = ["Neighborhood"]
parsed_df = get_parsed_df(input_file, columns)

# drop duplicate values
cleaned_df = parsed_df.drop_duplicates()

#transform data
transform_data(cleaned_df, output_file, table)