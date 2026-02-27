#Goal: create csv file that contains 1 column with object id
import pandas as pd

#prep data
list =[]
for i in range(1,10001):
    list.append(i)
fire_hydrant = {"object_id": list}

df = pd.DataFrame(fire_hydrant)
file_path = '../../csv_files/fire_hydrant.csv'

df.to_csv(file_path, index=False)