'''
0 X
1 Y
2 OBJECTID
3 Neighborhood
4 Address
5 Date_Inventoried
6 SPECIES
7 MATURE_SIZE
8 FUNCTIONAL_TYPE
9 DIAMETER
10 Condition
11 Site_Type
12 Site_Size
13 Site_Width
14 Wires
15 SITE_IMPROVEMENT
'''

import csv

def getDataset():
    with open('../Downloads/Street_Tree_Inventory_-_Active_Records.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        dataset=[]
        for row in csv_reader:
            dataset.append(row)
    #print(len(dataset))
    return dataset
def main():
    ds=getDataset()
    ds=ds[1:]#removes first header row
    ds_by_column=[[] for _ in range(16)]
    for row in ds:
        for c in range(len(row)):
            ds_by_column[c].append(row[c])
    query_list=""
    #query_list+=makeQuery("neighborhood",(ds_by_column[3]))
    query_list+=makeQuery("location_type_width",(ds_by_column[13],ds_by_column[12]))
    print(query_list)
    


def makeQuery(to_database,columns:tuple):
    big_text_block=""
    for c in list(zip(*columns)):#the * in front of columns separates into each item of the list
        big_text_block+=f"INSERT INTO {to_database} VALUES({c});\n"
    return big_text_block

if __name__ == "__main__":
    main()