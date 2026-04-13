<!DOCTYPE html>
<html>
  <head>
    <title>Results</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <?php
    //error reporting
    ini_set('display_errors',1);
    ini_set('display_startup_errors',1);
    error_reporting(E_ALL);

    include('functions.php');
    $dbc = db_connect();

    $selection = $_GET['query'];
    //transform selection to query
    $query = transform_selection($selection);
    $result = db_do_query($dbc,$query);

    echo '<p>
        <a href=index.html>&larr;</a>
        to go back </p>';
    echo '<p> Your query: ' . $query . '</p>';
    echo '<h2>'. 'Results' . '</h2>';

    //for data
    //for update, deletes
    if (is_int($result)){
    echo '<p> Affected rows:'  . $result;}
    //for selects
    else{
    $first_row = $result[array_key_first($result)];
    echo '<table>';
      echo '<tr>'; //for column names
        foreach (array_keys($first_row) as $column_name){
          echo '<th>' . $column_name . '</th>';}
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