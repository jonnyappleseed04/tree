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
        echo $input;
        $query = $input;
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


?>