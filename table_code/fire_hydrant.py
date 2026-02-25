#Goal: create sql file that inserts fire_hydrants in fire_hydrant table
#number of fire_hydrants are arbitrary
num_fire_hydrant = 10000
#.. = one level up
output_file = "../output_files/fire_hydrant.sql"

def gen_data(quantity, file):
    with open(file, 'w') as f:
        for i in range(quantity):
            query = (f"insert into fire_hydrant "
                     f"values (null);\n") #sql will catch 'null' and replace with index num
            f.write(query)

gen_data(num_fire_hydrant, output_file)