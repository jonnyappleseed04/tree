#Goal: create sql file that inserts fire_hydrants... in fire_hydrant... table
import pandas as pd
import random
#.. = one level up
input_file = "../csv_files/fire_hydrant.csv"
output_file = "../output_files/tree_is_next_to_fire_hydrant.sql"
min = 1
max = 252205
#create function that generates ran num between 1 and 252205 or null
def get_ran_value(min, max, null_prob=.5):
    if random.random() < null_prob:
        return "null"
    else:
        return random.randint(min, max)
# print(get_ran_value(min, max))

def transform_data(input_file, output_file): #transforms data into sql file
    df = pd.read_csv(input_file)
    with open(output_file, 'w') as f:
        for index, _ in enumerate(df.itertuples(), start=1):
             query = (f"insert into tree_is_next_to_fire_hydrant "
                      f"values ({get_ran_value(min, max)}, {index});\n") #sql will catch 'null' and replace with index num
             f.write(query)

transform_data(input_file, output_file)