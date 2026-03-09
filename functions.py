import pandas as pd
import random
#region
def get_ran_value(min, max, null_prob=.5):
    """Generates random number between min and max or null"""
    if random.random() < null_prob:
        return None
    else:
        return random.randint(min, max)
#endregion

#region
def create_insert_query(table, values:tuple):
    """Creates an insert query with given table and tuple of values"""
    query = f"insert into {table} values("

    for index, value in enumerate(values, start=1):
        # for int, float, null
        if (type(value) is int or type(value) is float
                or value == "null"):
            if len(values) != index:
                query += f"{value}, "
            else:
                query += f"{value});\n"
        #date note: gets rid of timestamp bc I thought it was irrelevant
        elif value.count("/")==2:
            mod_value = value.split(" ", 1)[0]
            if len(values) != index:
                query += f"\"{mod_value}\", "
            else:
                query += f"\"{mod_value}\");\n"
        # for string
        else:
            if len(values) != index:
                query += f"\"{value}\", "
            else:
                query += f"\"{value}\");\n"

    return query

def transform_data(df, sql_file, table):
    """Transforms data frame into sql file"""
    with open(sql_file, 'w') as f:
        for row in df.itertuples(index=False, name=None):
            query = create_insert_query(table, row)
            f.write(query)
#endregion

#region
def get_parsed_df(csv, columns_to_get:list):
    """Returns a parsed data frame given csv file and list of columns to get"""
    # .fillna is to replace "nans" with "nulls"
    df = pd.read_csv(csv).fillna("null")
    new_df = df[columns_to_get].copy()
    return new_df
#endregion

#region
#Specify columns that are not null using their index in the list
#note: not null may not be necessary as line 10718 is the limit of csv viewer

def transfer_data(input_csv_file_path:str, output_sql_file_path:str, table_name:str, 
                  columns_to_get:list = False, not_null:list = False, auto_increment = False):
    """Converts csv file into parsed df, drops redundant rows, adds auto_increment column, and converts df to sql queries"""
    #parse data if necessary
    if columns_to_get:
        parsed_df = get_parsed_df(input_csv_file_path, columns_to_get)
    else:
        # .fillna() is to replace "nans" with "nulls"
        parsed_df = pd.read_csv(input_csv_file_path).fillna("null")

    # drop redundant rows
    cleaned_df = parsed_df.drop_duplicates()

    #drop rows that have null value in not null column
    if not_null:
        #new list with only not null columns
        not_null_columns = [columns_to_get[index] for index in not_null]
        cleaned_df = cleaned_df[~cleaned_df[not_null_columns].eq("null").any(axis=1)]

    #add auto_increment column
    if auto_increment:
        #this kinda makes auto_increment in schema pointless
        object_id = 1
        cleaned_df.insert(0, 'auto_increment',
                          range(object_id, object_id+len(cleaned_df)))
    # transform data
    transform_data(cleaned_df, output_sql_file_path, table_name)

#endregion

