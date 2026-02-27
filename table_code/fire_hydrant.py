#Goal: create sql file that inserts fire_hydrants in fire_hydrant table
import pandas as pd
#.. = one level up
input_file = "../csv_files/fire_hydrant.csv"
output_file = "../output_files/fire_hydrant.sql"

def transform_data(input_file): #transforms data into sql file (not done)
    df = pd.read_csv(input_file)
    with open(output_file, 'w') as f:
        for _ in df.itertuples():
             query = (f"insert into fire_hydrant "
                      f"values (null);\n") #sql will catch 'null' and replace with index num
             f.write(query)
