
<!DOCTYPE html>
<html>
  <head>
    <title>Results</title>
  </head>
  <body>
    <?php
    ini_set('display_errors',1);
    ini_set('display_startup_errors',1);
    error_reporting(E_ALL);

    $selection = $_GET['query'];
    include('functions.php');
    $dbc = db_connect();
    //transform selection to query
    $query = transform_selection($selection);
    //other stuff
    $result = db_do_query($dbc,$query);

    echo '<p> Your query: ' . $query . '</p>';
    echo '<p> press
        <a href = index.html>this</a>
        to go back </p>';
    echo '<h2>'. 'results' . '</h2>';

    //for data
    //for update, deletes
    if (is_int($result)){
    echo '<p> Affected rows:'  . $result;}
    else{
    $first_row = $result[array_key_first($result)];
    echo '<table>';
      echo '<tr>'; //for column names
        foreach (array_keys($first_row) as $column_name){
          echo '<td>' . $column_name . '</td>';}
      echo '</tr>';
    foreach ($result as $row) {
    //foreach is specific loop for arrays
      echo '<tr>'; //table row

      foreach ($row as $value){
        echo '<td>' . $value . '</td>';
      }
      echo '</tr>';
    }

    echo '</table>';
    }

?>
  </body>
</html>