# SI664-scripts
Miscellaneous Python scripts

## 1.0 Install
Either fork this repo and then clone to your working directory or download a *.zip file of the code. Create a virtual environment and then run `pip` to install package dependencies listed in the `requirements.txt` file. 

### macOS
```commandline
$ cd path/to/SI664/scripts
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

### Windows
```commandline
> cd path/to/SI664/scripts
> venv\Scripts\activate
(venv) > pip install -r requirements.txt
```

## 2.0 Available scripts

### 2.1 run_mysql_script.py
This python script is designed to process MySQL scripts.  The script requires a valid database 
connection.  After opening a connection and creating a cursor, the script creates a list of SQL 
statements after splitting the SQL script on each semi-colon encountered (;).  The script then 
loops through the statements, attempting to execute each. If successful, the script commits the 
changes, closes the cursor and then closes the connection.  Otherwise, it rolls back the 
transaction and reports the error encountered.

optional arguments:
* -h, --help (show this help message and exit)
* -c, --config (path to config file)
* -p, --path (path to script)

Run as follows, tailoring the *.yaml and *.sql file paths as necessary:

```commandline
(venv) $ python run_mysql_script.py -c ./path/to/config/file/*.yaml -p ./path/to/sql/script/*.sql
```

### 2.1 inspect_un_data_sets.py
Run `inspect_un_data_sets.py` to "inspect" two UN data sets included in the project `/input` directory:

* un_area_country_codes-m49.csv
* unesco_heritage_sites.csv

The script utilizes the [Pandas](https://pandas.pydata.org/) library to peruse the data sets, 
generating a set of column-based *.csv files that contain distinct column values (duplicate 
values and NaN values are filtered out) sorted in ascending order.  The files are stored in the 
project `/output` directory.

#### macOS
```commandline
(venv) $ python3 inspect_un_data_sets.py
```

##### Output

```commandline
INFO: Source file read /absolute/path/to/input/un_area_country_codes-m49.csv
INFO: UNSD M49 regions written to file /absolute/path/to/output/unsd_region.csv
INFO: UNSD M49 sub-regions written to file /absolute/path/to/output/unsd_sub_region.csv
INFO: UNSD M49 intermediate regions written to file /absolute/path/to/output/unsd_intermed_region.csv
INFO: UNSD M49 countries and areas written to file /absolute/path/to/output/unsd_country_area.csv
INFO: UNSD M49 development status written to file /absolute/path/to/output/unsd_dev_status.csv
INFO: Source file read /absolute/path/to/input/unesco_heritage_sites.csv
INFO: UNESCO heritage site countries/areas written to file /absolute/path/to/output/unesco_heritage_site_country_area.csv
INFO: UNESCO heritage site categories written to file /absolute/path/to/output/unesco_heritage_site_category.csv
INFO: UNESCO heritage site regions written to file /absolute/path/to/output/unesco_heritage_site_region.csv
INFO: UNESCO heritage site transboundary values written to file /absolute/path/to/output/unesco_heritage_site_transboundary.csv
```

#### Windows 10
```commandline
(venv) > python inspect_un_data_sets.py
```

##### Output

```commandline
INFO: Source file read C:\path\to\input\un_area_country_codes-m49.csv
INFO: UNSD M49 regions written to file C:\path\to\output\unsd_region.csv
INFO: UNSD M49 sub-regions written to file C:\path\to\output\unsd_sub_region.csv
INFO: UNSD M49 intermediate regions written to file C:\path\to\output\unsd_intermed_region.csv
INFO: UNSD M49 countries and areas written to file C:\path\to\output\unsd_country_area.csv
INFO: UNSD M49 development status written to file C:\path\to\output\unsd_dev_status.csv
INFO: Source file read C:\path\to\input\unesco_heritage_sites.csv
INFO: UNESCO heritage site countries/areas written to file C:\path\to\output\unesco_heritage_site_country_area.csv
INFO: UNESCO heritage site categories written to file C:\path\to\output\unesco_heritage_site_category.csv
INFO: UNESCO heritage site regions written to file C:\path\to\output\unesco_heritage_site_region.csv
INFO: UNESCO heritage site transboundary values written to file C:\path\to\output\unesco_heritage_site_transboundary.csv
```
