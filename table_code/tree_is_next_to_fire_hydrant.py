#Goal: create sql file that inserts fire_hydrants... in fire_hydrant... table
from functions import *
#.. = one level up
input_file = "../csv_files/tree_is_next_to_fire_hydrant.csv"
output_file = "../output_files/tree_is_next_to_fire_hydrant.sql"
table = "tree_is_next_to_fire_hydrant"
columns = ["fk_tree","fk_fire_hydrant"]

transfer_data(input_file,output_file,table,columns,
              not_null=[0,1])