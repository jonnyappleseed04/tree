/*
tree database
version 2.1
date 2/23/2026
authors: Amelia, Jonathan
*/


/*
Regarding lengths of attributes--
The database was put into a function that calculated the maximum # of characters for non-numeric columns, resulting:
Neighborhood : 23
Address : 59
SPECIES : 79
MATURE_SIZE : 7
FUNCTIONAL_TYPE : 20
Condition : 9
Site_Type : 21
Site_Size : 6
Wires : 12
SITE_IMPROVEMENT : 13.


Other functions were used to acquire numerical maximums:
X : 13 total, 4 after '.'
Y : 11 total, 4 after '.'
DIAMETER : 11 total, 9 after '.'
Site_Width : 12 total, 9 after '.'


OBJECTID : 6 digits (Automatically increasing)
Date_Inventoried : Date


If more data was intended to be collected, maximums would be increased
*/


drop database if exists tree;
create database tree;
use tree;


create table neighborhood(
neighborhood_name varchar(23),
primary key (neighborhood_name)
);


-- plural table below:
create table neighborhood_address(
fk_neighborhood varchar(23),
address varchar(59),
primary key (fk_neighborhood, address),
foreign key (fk_neighborhood) references neighborhood(neighborhood_name)
  on update cascade
  on delete cascade
);


create table location_type(
location_id int ,
site_type varchar(21),
width decimal(12,9),
size varchar(6),
improvement varchar(13),
wires varchar(12),
primary key (location_id)
);


create table coordinates(
x decimal(13,4),
y decimal(11,4),
primary key (x, y),
fk_neighborhood varchar(23),
fk_location_type int not null, -- for many-to-one. not null bc location type is required.
foreign key (fk_neighborhood) references neighborhood(neighborhood_name)
  on update cascade
  on delete cascade,
foreign key (fk_location_type) references location_type(location_id)
  on update cascade
  on delete cascade
);


create table tree_basic(
object_id int auto_increment,
date_inventoried date,
fk_coordinates_x decimal(13,4),
fk_coordinates_y decimal(11,4),
primary key (object_id),
foreign key (fk_coordinates_x, fk_coordinates_y) references coordinates(x, y)
  on update cascade
  on delete cascade
);


-- normalization table below:
create table tree_details_species(
species varchar(79),
functional_type varchar(20),
primary key (species)
);


create table tree_details(
mature_size varchar(7),
diameter decimal(11,9),
item_condition varchar(9),
species varchar(79),
fk_tree int,
primary key (fk_tree), -- SINGULAR weak table's foreign is also the primary key
foreign key (fk_tree) references tree_basic(object_id)
  on update cascade
  on delete cascade,
foreign key (species) references tree_details_species (species)
);


create table fire_hydrant(
object_id int auto_increment,
color VARCHAR(6),
primary key (object_id)
);


create table tree_is_next_to_fire_hydrant(
fk_tree int,
fk_fire_hydrant int,
primary key (fk_tree, fk_fire_hydrant),
foreign key (fk_tree) references tree_basic(object_id)
  on update cascade
  on delete cascade,
foreign key (fk_fire_hydrant) references fire_hydrant(object_id)
  on update cascade
  on delete cascade
);