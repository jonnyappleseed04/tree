#neighborhood
from jon_functions import *
from pathlib import Path
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/neighborhood.sql"
table = "neighborhood"
columns = ["Neighborhood"]

transfer_data(input_file, output_file, table, columns_to_get=columns)

#neighborhood_address
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/neighborhood_address.sql"
table = "neighborhood_address"
columns = ["Neighborhood", "Address"]

transfer_data(input_file, output_file, table, columns_to_get=columns)

#location_type
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/location_type.sql"
table = "location_type"
columns = ["Site_Type", "Site_Width", "Site_Size", "SITE_IMPROVEMENT", "Wires"]

transfer_data(input_file, output_file, table, columns_to_get=columns,
              auto_increment=True)

#coordinates
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

#tree
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/tree.sql"
table = "tree"
columns = ["OBJECTID","Date_Inventoried","X","Y"]

transfer_data(input_file, output_file, table,
              columns_to_get=columns)

#fire_hydrant
#.. = one level up
input_file = "../csv_files/fire_hydrant.csv"
output_file = "../output_files/fire_hydrant.sql"
table = "fire_hydrant"

transfer_data(input_file,output_file,table)

#tree_is_next_to_fire_hydrant
#.. = one level up
input_file = "../csv_files/tree_is_next_to_fire_hydrant.csv"
output_file = "../output_files/tree_is_next_to_fire_hydrant.sql"
table = "tree_is_next_to_fire_hydrant"
columns = ["fk_tree","fk_fire_hydrant"]

transfer_data(input_file,output_file,table,columns,
              not_null=[0,1])

#tree_details_species
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/tree_details_species.sql"
table = "tree_details_species"
columns = ["SPECIES","FUNCTIONAL_TYPE"]

transfer_data(input_file, output_file, table,
              columns_to_get=columns)

#tree_details
#.. = one level up
input_file = "../csv_files/tree_inventory.csv"
output_file = "../output_files/tree_details.sql"
table = "tree_details"
columns = ["MATURE_SIZE","DIAMETER", "Condition",
           "SPECIES", "OBJECTID"]

transfer_data(input_file, output_file, table,
              columns_to_get=columns)

#combining output files into one
folder_path = Path("../output_files")
output_file = "../combined_queries.sql"

files = sorted(folder_path.glob("*.sql"),
               key=lambda f: f.stat().st_mtime)

with open(output_file, "w") as outfile:
    for file_path in files:
        with open(file_path, "r") as infile:
            outfile.write(infile.read() + "\n")