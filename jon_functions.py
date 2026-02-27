#this is just temporary file to store my functions
#ik this is kinda messy rn
import pandas as pd
import random
#for data generation
#region
#create function that generates ran num between 1 and 252205 or null
def get_ran_value(min, max, null_prob=.5):
    if random.random() < null_prob:
        return "null"
    else:
        return random.randint(min, max)
#endregion

#for transforming data from csv to sql queries
# region
#function to create insert query given table and set of values
def create_insert_query(table, values:tuple):
    query = f"insert into {table} values("

    for index, value in enumerate(values, start=1):
        if len(values) != index:
            query += f"{value}, "
        else:
            query += f"{value});\n"

    return query

#transforms csv data into sql file
def transform_data(csv_file, sql_file, table):
    # .fillna is to replace "nans" with "nulls"
    df = pd.read_csv(csv_file).fillna("null")

    with open(sql_file, 'w') as f:
        for row in df.itertuples(index=False, name=None):
            query = create_insert_query(table, row)
            f.write(query)
#endregion

#for parsing csv files
