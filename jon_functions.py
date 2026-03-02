#this is just temporary file to store my functions
#ik this is kinda messy rn
import duckdb
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
        # for int, float, null or date
        if (type(value) is int or type(value) is float
                or value.count("/")==2 or value == "null"):
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
    # .fillna is to replace "nans" with "nulls"
    df = pd.read_csv(csv).fillna("null")
    new_df = df[columns_to_get].copy()
    return new_df

#function to get rid of dublicate values in column
#df.drop_duplicates()
#endregion

#combining all functions
#region
#Specificy columns that are not null
#using their index in the list"
#note: not null may not be necessary as line 10718 is the limit of csv viewer

#function that converts csv file into parsed df,
#drops redundant rows, adds auto_increment column,
#and converts df to sql queries
def transfer_data(input_csv_file_path:str, output_sql_file_path:str,
                  table_name:str, columns_to_get:list = False, not_null:list = False, auto_increment = False):
    #parse data if necessary
    if columns_to_get:
        parsed_df = get_parsed_df(input_csv_file_path, columns_to_get)
    else:
        # .fillna is to replace "nans" with "nulls"
        parsed_df = pd.read_csv(input_csv_file_path).fillna("null")

    # drop redundant rows
    cleaned_df = parsed_df.drop_duplicates()

    #drop rows that have null value in not null column
    if not_null:
        #new list with only not null columns
        not_null_columns = [columns_to_get[index] for index in not_null]
        for columns in not_null_columns:
            cleaned_df = cleaned_df[~cleaned_df[columns] == 'null']

    #add auto_increment column
    if auto_increment:
        #this kinda makes auto_increment in schema pointless
        object_id = 1
        cleaned_df.insert(0, 'auto_increment',
                          range(object_id, object_id+len(cleaned_df)))
    # transform data
    transform_data(cleaned_df, output_sql_file_path, table_name)

#endregion

