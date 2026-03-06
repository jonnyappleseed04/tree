#create csv file that generates columns
#in tree_is_next_to_fire_hydrant
from functions import *
import pandas as pd
min = 1
max = 252205

#prep data
fk_fire_hydrant =[]
for i in range(1,10001):
    fk_fire_hydrant.append(i)

fk_tree = []
for _ in fk_fire_hydrant:
    fk_tree.append(get_ran_value(min, max))

tree_is_next_to_fire_hydrant = {"fk_fire_hydrant": fk_fire_hydrant,
                                "fk_tree": fk_tree}
#write
df = pd.DataFrame(tree_is_next_to_fire_hydrant)
file_path = '../../csv_files/tree_is_next_to_fire_hydrant.csv'
df.to_csv(file_path, index=False)