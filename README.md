# Project: Extract, Transform, Load

This is a team project. Work on it with your assigned team. Only one of you
needs to turn it in — but make sure someone does!

## Objectives

* Build a program extracting the relevant data from the [City of Portland Tree
  Inventory](https://gis-pdx.opendata.arcgis.com/datasets/c2b02440053f459db71e1109b9947e51_1415/explore)
  dataset,
* Depending on your ER diagram, use other data sources or generate the necessary
  synthetic data,
* Output the processed data, for each of the tables in your schema, into one or
  more files, and
* Test your output by loading the extracted data into your database.

## Details

Write a program that reads the raw data, generate any synthetic data, extract
and if necessary transform the data relevant to your database design, break the
data into the necessary tables including any needed junction tables, and output
this data into distinct CSV files (one per table) or one or more SQL scripts.

Use your favorite programming language (Python is recommended). Follow
recommended programming style including appropriate documentation.

Test your output by going to phpMyAdmin and selecting your database (make sure
you have completed the previous assignment first).  Then for each file:

* Click on “Import”
* Select the file
* The appropriate format should be automatically selected for you
* If necessary, decent format-specific options are also selected for you
* Click on "Go"

Browse the data to see if data appears to have loaded properly. Then, in the
“SQL” tab, enter a few queries to confirm that all the data appears to be
present. In particular, issue the appropriate SQL query in the “SQL” tab of
phpMyAdmin to find the number of rows in each table and compare against expected
values.

## Hints

* Start small (i.e., process a subset of the entire dataset, generate data for
  a single table first, etc.).
* Expect to have to break some output files into multiple files; phpMyAdmin
  limits the size of the CSV files it can import.
* Using the MySQL REPL and input redirection (i.e., `mysql -u tree -p <
  csv-file-or-sql-script`) may avoid issues around file sizes.

## What to turn in

Hand in `etl.py`.

If you had to make modifications to deliverables of previous project steps,
please include the modified files in your submission.

Your program should include the names of all participants in your group (if one
person didn't contribute, don't include their name).
