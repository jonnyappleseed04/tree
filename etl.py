#Amelia & Jonathan
from functions import *
from pathlib import Path
#generate data
#region
#generate fire_hydrant_data
#region
#prep data
list_ =[]
for i in range(1,10001):
    list_.append(i)
fire_hydrant = {"object_id": list_}

df = pd.DataFrame(fire_hydrant)
file_path = 'csv_files/fire_hydrant.csv'

df.to_csv(file_path, index=False)
#endregion
#create csv file that generates columns
#in tree_is_next_to_fire_hydrant
#region
min_ = 1
max_ = 252205

#prep data
fk_fire_hydrant =[]
for i in range(1,10001):
    fk_fire_hydrant.append(i)

fk_tree = []
for _ in fk_fire_hydrant:
    fk_tree.append(get_ran_value(min_, max_))

tree_is_next_to_fire_hydrant = {"fk_fire_hydrant": fk_fire_hydrant,
                                "fk_tree": fk_tree}
#write
df = pd.DataFrame(tree_is_next_to_fire_hydrant)
file_path = 'csv_files/tree_is_next_to_fire_hydrant.csv'
df.to_csv(file_path, index=False)
#endregion
#endregion
#create table queries
#region
#neighborhood
#region
#.. = one level up
input_file = "csv_files/tree_inventory.csv"
output_file = "output_files/neighborhood.sql"
table = "neighborhood"
columns = ["Neighborhood"]

transfer_data(input_file, output_file, table, columns_to_get=columns)
#endregion
#neighborhood_address
#region
input_file = "csv_files/tree_inventory.csv"
output_file = "output_files/neighborhood_address.sql"
table = "neighborhood_address"
columns = ["Neighborhood", "Address"]

transfer_data(input_file, output_file, table, columns_to_get=columns)
#endregion
#location_type
#region
#.. = one level up
input_file = "csv_files/tree_inventory.csv"
output_file = "output_files/location_type.sql"
table = "location_type"
columns = ["Site_Type", "Site_Width", "Site_Size", "SITE_IMPROVEMENT", "Wires"]

transfer_data(input_file, output_file, table, columns_to_get=columns,
              auto_increment=True)
#endregion
#coordinates
#region
#.. = one level up
input_file = "csv_files/tree_inventory.csv"
output_file = "output_files/coordinates.sql"
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
#endregion
#tree
#region
#.. = one level up
input_file = "csv_files/tree_inventory.csv"
output_file = "output_files/tree.sql"
table = "tree"
columns = ["OBJECTID","Date_Inventoried","X","Y"]

transfer_data(input_file, output_file, table,
              columns_to_get=columns)
#endregion
#fire_hydrant
#region
#.. = one level up
input_file = "csv_files/fire_hydrant.csv"
output_file = "output_files/fire_hydrant.sql"
table = "fire_hydrant"

transfer_data(input_file,output_file,table)
#endregion
#tree_is_next_to_fire_hydrant
#region
#.. = one level up
input_file = "csv_files/tree_is_next_to_fire_hydrant.csv"
output_file = "output_files/tree_is_next_to_fire_hydrant.sql"
table = "tree_is_next_to_fire_hydrant"
columns = ["fk_tree","fk_fire_hydrant"]

transfer_data(input_file,output_file,table,columns,
              not_null=[0,1])
#endregion
#tree_details_species
#region
#.. = one level up
input_file = "csv_files/tree_inventory.csv"
output_file = "output_files/tree_details_species.sql"
table = "tree_details_species"
columns = ["SPECIES","FUNCTIONAL_TYPE"]

transfer_data(input_file, output_file, table,
              columns_to_get=columns)
#endregion
#tree_details
#region
#.. = one level up
input_file = "csv_files/tree_inventory.csv"
output_file = "output_files/tree_details.sql"
table = "tree_details"
columns = ["MATURE_SIZE","DIAMETER", "Condition",
           "SPECIES", "OBJECTID"]

transfer_data(input_file, output_file, table,
              columns_to_get=columns)
#endregion
#endregion
#optionally combines output files into one
#named combined_queries.sql
#region
folder_path = Path("output_files")
output_file = "combined_queries.sql"

files = sorted(folder_path.glob("*.sql"),
               key=lambda f: f.stat().st_mtime)

with open(output_file, "w") as outfile:
    for file_path in files:
        with open(file_path, "r") as infile:
            outfile.write(infile.read() + "\n")
#endregion