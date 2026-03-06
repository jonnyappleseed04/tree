#Goal: insert relevant data into tree table
from functions import *
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/coordinates.sql"
table = "coordinates"
columns = ["X", "Y", "Neighborhood",
        "Site_Type", "Site_Width", "Site_Size",
           "SITE_IMPROVEMENT", "Wires"]

#get df of location_type
columns_2 = ["Site_Type", "Site_Width", "Site_Size", "SITE_IMPROVEMENT", "Wires"]
parsed_location_type = get_parsed_df(input_file, columns_2)
cleaned_location_type = parsed_location_type.drop_duplicates()
#adds object_ID
object_id = 1
cleaned_location_type.insert(0, 'object_id',
                range(object_id, object_id+len(cleaned_location_type)))

#create df w/ coordinates + Neighborhood + columns_2
raw_data = get_parsed_df(input_file, columns)

#join
raw_coordinates = raw_data.merge(
    cleaned_location_type[columns_2 +['object_id']], #only pulls object_id
    on= columns_2,
    how='left'
)
cleaned_coordinates =  raw_coordinates.drop(columns_2, axis=1)
#this code checks that all foreign keys (object_id)
#has a reference
# result = cleaned_coordinates['object_id']
# result_m = result.drop_duplicates()

#check for duplicate composite key
# duplicates = cleaned_coordinates[cleaned_coordinates.duplicated(
#     subset=['X', 'Y'], keep=False)]
#has a couple of duplicates so I'm going to clean data
cleaned_coordinates.drop_duplicates(inplace=True)

transform_data(cleaned_coordinates, output_file, table)