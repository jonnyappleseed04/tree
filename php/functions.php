<?php
    ini_set('display_errors',1);
    ini_set('display_startup_errors',1);
    error_reporting(E_ALL);

    function db_connect() {
        define('DB_USER', 'tree');
        define('DB_PASSWORD', '');
        define('DB_HOST', 'localhost');
        define('DB_NAME', 'tree');

        ($dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME))
        || die('Could not connect to MariaDB: ' . mysqli_connect_error());
        return $dbc;
    }


    function db_get_id_and_classes($dbc) {
        $query = 'SELECT id, name FROM course group by name';
        $response = mysqli_query($dbc, $query);
        if ($response) {
            $arr = [];
            while ($row = mysqli_fetch_array($response)) {
                array_push($arr, $row);
            }
            return $arr;
        }
        else {
            die('Couldn\'t issue database query: ' . mysqli_error($dbc));
        }
    }

    function db_get_students_from_class($dbc, $class_id){
        $query =    'SELECT student.name FROM student 
                    join student_takes_course on student.id = student_takes_course.student_id 
                    where student_takes_course.course_id = ' . $class_id;
        $response = mysqli_query($dbc, $query);
        if ($response) {
            $arr = [];
            while ($row = mysqli_fetch_array($response)) {
                array_push($arr, $row);
            }
            return $arr;
        }
        else {
            die('Couldn\'t issue database query: ' . mysqli_error($dbc));
        }

    }

    function db_get_class_name_from_id ($dbc, $c_id){
        $query = 'SELECT name from course where id = '.$c_id;
        $response = mysqli_query($dbc, $query);
        if ($response) {
            return $row = mysqli_fetch_array($response);
        }
        else {
            die('Couldn\'t issue database query: ' . mysqli_error($dbc));
        }
    }
    function db_get_class_names_from_string($dbc, $input){
        $query =    'SELECT name FROM course
                    where name like "%' . $input . '%";';
        $response = mysqli_query($dbc, $query);
        if ($response) {
            $arr = [];
            while ($row = mysqli_fetch_array($response)) {
                array_push($arr, $row);
            }
            return $arr;
        }
        else {
            die('Couldn\'t issue database query: ' . mysqli_error($dbc));
        }

    }
    function db_do_query($dbc, $input){
        $query = $input;
        $response = mysqli_query($dbc, $query);

        if ($response instanceof mysqli_result) { //checks if response is type result
        $arr = [];
        while ($row = mysqli_fetch_assoc($response)) {
            array_push($arr, $row);
        }
        return $arr;
        }
        elseif ($response === true) {
        return mysqli_affected_rows($dbc);
        }
        else {
        die('Couldn\'t issue database query: ' . mysqli_error($dbc));
        }

    }
    //transforms selection to query
    function transform_selection($selection){
        $queries = [
            "1" => "select * from tree_basic where object_id = 69830;",
            "2" => "select tree_basic.object_id, fk_neighborhood, site_type
                    from tree_basic
                    join coordinates on tree_basic.fk_coordinates_x = coordinates.x
                    and tree_basic.fk_coordinates_y = coordinates.y
                    join location_type on fk_location_type = location_id
                    where fk_neighborhood = \"SELLWOOD-MORELAND\" and site_type = \"Median\";",
            "3" => "select neighborhood_name, count(*) as tree_num
                    from neighborhood, coordinates
                    where neighborhood_name = fk_neighborhood
                    group by neighborhood_name
                    order by tree_num desc
                    limit 10;",
            "4" => "Insert into tree_basic (date_inventoried)
	                values('2026/03/16');",
            "5" => "select neighborhood_name, object_id, date_inventoried
                    from neighborhood
                    join coordinates
                    on fk_neighborhood = neighborhood_name
                    inner join tree_basic
                    on fk_coordinates_x = x and fk_coordinates_y = y
                    where neighborhood_name = 'Crestwood'
                    order by object_id, date_inventoried;",
            "6" => "select fk_neighborhood, count(*)
                    from tree_basic
                    join coordinates on tree_basic.fk_coordinates_x = coordinates.x
                    and tree_basic.fk_coordinates_y = coordinates.y
                    join tree_is_next_to_fire_hydrant on tree_basic.object_id = tree_is_next_to_fire_hydrant.fk_tree
                    GROUP BY fk_neighborhood;",
            "7" => "select object_id as tree, x, y, neighborhood_name as neighborhood
                    from tree_basic
                    join coordinates
                    on fk_coordinates_x = x and fk_coordinates_y = y
                    join neighborhood
                    on fk_neighborhood = neighborhood_name
                    where (x between (select min(x) from coordinates)
                               and (select min(x)+10000 from coordinates)) -- range can be changed
                    and (y between (select min(y) from coordinates)
                             and (select min(y)+10000 from coordinates)) -- same here
                    order by x;",
            "8" => "create view coordinates_view
                    as select min(x) as min_x, max(x) as max_x, max(x)-min(x) as
                    range_x, min(y) as min_y, max(y) as max_y, max(y)-min(y) as
                    range_y
	                from coordinates;",
            "9" => "select object_id as tree, x, y, neighborhood_name, count(*) as fire_hydrants
                    from coordinates
                    join neighborhood
                    on fk_neighborhood = neighborhood_name
                    inner join tree_basic
                    on fk_coordinates_x = x and fk_coordinates_y = y
                    inner join tree_is_next_to_fire_hydrant
                    on object_id = fk_tree
                    group by fk_tree
                    having fire_hydrants != 1;",
            "10" => "create view tree_info
                    as select object_id, date_inventoried, fk_coordinates_x as x,
                    fk_coordinates_y as y, mature_size, diameter, item_condition, species
                    from tree_basic, tree_details
                    where fk_tree = object_id;",
            "11" => "insert into fire_hydrant (color)
                    values ('orange');",
            "12" => "delete from fire_hydrant
                    where object_id = (select max(object_id) from fire_hydrant);"
        ];
        echo array_key_exists($selection,$queries);
        if (array_key_exists($selection,$queries)){
            return $queries[$selection];
        }
        return $selection;
    }



?>