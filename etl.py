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
    values=[[] for _ in range(16)]
    for row in ds:
        for c in range(len(row)):
            values[c].append(row[c])
    print(values[0][1:11])

if __name__ == "__main__":
    main()