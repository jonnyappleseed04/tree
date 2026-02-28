#Goal: create sql file that inserts fire_hydrants in fire_hydrant table
from jon_functions import *
#.. = one level up
input_file = "../csv_files/fire_hydrant.csv"
output_file = "../output_files/fire_hydrant.sql"
table = "fire_hydrant"

transfer_data(input_file,output_file,table)

