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
        # for int, float, or date
        if type(value) is int or type(value) is float or value.count("/")==2:
            if len(values) != index:
                query += f"{value}, "
            else:
                query += f"{value});\n"
        # for string
        else:
            if len(values) != index:
                query += f"\"{value}\", "
            else:
                query += f"\"{value}\");\n"

    return query

#transforms data frame into sql file
def transform_data(df, sql_file, table):
    with open(sql_file, 'w') as f:
        for row in df.itertuples(index=False, name=None):
            query = create_insert_query(table, row)
            f.write(query)
#endregion

#for parsing csv files
#region
#function that returns a parsed data frame given csv file and list of columns to get
def get_parsed_df(csv, columns_to_get:list):
    df = pd.read_csv(csv)
    new_df = df[columns_to_get].copy()
    return new_df

#function to get rid of dublicate values in column
#df.drop_duplicates()
#endregion
