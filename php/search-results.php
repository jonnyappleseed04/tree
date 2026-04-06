<!DOCTYPE html>
<html>
  <head>
    <title>Results</title>
  </head>
  <body>
    <?php
    $search_string = $_GET['search_string'];
    include('functions.php');
    $dbc = db_connect();
    $result = db_do_query($dbc,$search_string);
  // if (count($result)==0){
  //   echo 'No classes with "'.$search_string.'" were found.';
  // }
  // else{
    echo '<table>';
    echo '<tr><td><b>Name</b></td></tr>';
    foreach ($result as $row) {
      echo '<tr>';

      for ($column = 0; $column<count($row)-2;$column +=1){
        echo '<td>' . $row[$column] . '</td>';
      }
      echo '</tr>';
    }

    echo '</table>';
  // }    
?>
  </body>
</html>