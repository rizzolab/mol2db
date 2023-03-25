# mol2db 0.0.1

Mol2db is a python-based software to interface with your mol2-based molecular library database on a linux-based command line. The database utitlizes psql to organize and store your mol2 molecules. Instead of storing your mol2 molecules into a multi-mol2 file format, which can be in the order of millions of molecules, you can store them in a SQL-based database by using mol2db commands.  


## requirements
Pyinstaller is necessary to install if you want a binary, but you can call the main function from the build by using python3. 
Pandas, psycopg (not psycopg2), and psql are required to install this build

To install pyinstaller
To install:
```
pip install pyinstaller
```

Pandas is a data manipulation tool. 
To install: 
```
pip install pandas
```

psycopg is a PostgreSQL python adaptor. This build does not use psycopg2.
To install:
```
pip install psycopg
```

psql (PostgreSQL) is a open source object-relational database system.
Please make sure you are not disrupting anybody's workflow/data if psql.
is already in your environment. 
To install:
```
apt-get install postgresql-12
```

If you are having trouble figuring out how to set up psql after installing it.
This [link](https://pimylifeup.com/raspberry-pi-postgresql/) is helpful to set up psql



## To install mol2db

```
cd mol2db
make mol2db
```


To clean:
```
make clean
```

## How it works

The general workflow:

Mol2 files are converted into csv files, then these csv files can be imported into your generated psql database

You create a molecular table that is in that database.

While the mol2s are stored into your database, you can pull molecules out based on their cheminformatic
descriptors or by their IDs.

Below are column label for a molecular table. These are the available descriptors you can pull. 
The first column is the label of the descriptors. The second column is the datatype of that descriptor. 

```
      NUM_ATOMS         INT,
      NUM_BONDS         INT,
      MW            DECIMAL,
      ROT_BONDS         INT,
      FORMAL_CHARGE DECIMAL,
      HBA               INT,
      HBD               INT,
      HEAVY_ATOMS       INT,
      NUM_AROM          INT,
      NUM_ALIP          INT,
      NUM_SAT           INT,
      NUM_STEREO        INT,
      NUM_SPIRO         INT,
      LOGP          DECIMAL,
      TPSA          DECIMAL,
      SYNTHA        DECIMAL,
      QED           DECIMAL,
      LOGS          DECIMAL,
      NUM_PAINS         INT,
      PAINS_NAMES      TEXT,
      SMILES           TEXT

```
###################################

To convert a mol2 file into a `mol2db` compatible csv file.
```
m2db mol2csv -i input.mol2 -o output.csv
```

Then create a new database:
```
m2db --autocommit create DATABASE_NAME
```

Set up your configuration file for you psql access.
This command will make these flags as default psql credential information
into your psql database. An example:
```
m2db -d DATABASE_NAME -u USER_NAME createsource 
```

NOTE: Whenever mol2db is asking for your password, this is the password to your psql database that is associated with your username. If your adminstrator doesn't require you to have a pw, you can say no. Otherwise, the config file does store your password however it is not in plain text. The pw is hashed to bolster security. 

Then create psql molecular table:
```
m2db --autocommit moltables
```

Then insert the .csv file into the table:
```
m2db --autocommit csv2psql output.csv
```

If you want to pull molecules by ID. Make sure the ID.txt file contains all of the IDs
that are found in the psql library:
```
m2db pull_mols -i ID.txt
```


## How to edit your credentials
If you want to save your credentials rather than inputting flags for 
every request:

```
m2db -d DIFFERENT_DATABASE_NAME -u DIFFERENT_USER_NAME createsource 
```

If you want to update your credentials:

```
m2db -d CHANGED_DATABASE_NAME -u CHANGED_USER_NAME updatesource
```


If you want help:
```
m2db --help
```

output:

```
usage: mol2db [-h] [--autocommit] [-d DBNAME] [-ur USER_NAME] [-ht HT] [-pt PRT] [-cr [CRED]] [-v]
              {createsource,deletesource,updatesource,mol2csv,csv2mol2,execute,csv2psql,moltables,pull_mols,pull_by_des,pull_by_range,create,delete,ifex} ...

positional arguments:
  {createsource,deletesource,updatesource,mol2csv,csv2mol2,execute,csv2psql,moltables,pull_mols,pull_by_des,pull_by_range,create,delete,ifex}
                        help for subcommand
    createsource        to create credential file as the psql info.
    deletesource        to delete mol2db.config as the psql info
    updatesource        update the configuration file.
    mol2csv             to convert molecules into csv
    csv2mol2            to convert csv file into mol2 file
    execute             to execute a sql string
    csv2psql            to load up csv into db
    moltables           to create a molecular table
    pull_mols           to pull molecule(s) via text file
    pull_by_des         to pull molecules by descriptors
    pull_by_range       to pull molecules by descriptors based on a lower and upper range
    create              to create your own db. This command will initially connect db named "postgres" under your username. This should be created by default when installing
                        psql. Then it will create the dbname of your choice. Please do not delete or change that name
    delete              to delete your own db. This command will initially connect db named "postgres" under your username. This should be created by default when installing
                        psql. Then it will create the dbname of your choice. Please do not delete or change that name
    ifex                if components of psql exists

optional arguments:
  -h, --help            show this help message and exit
  --autocommit          specify if you want to autocommit(True) or not(False). No flag (False)
  -d DBNAME, --dbname DBNAME
                        enter your database name to access
  -ur USER_NAME, --user USER_NAME
                        enter your user name
  -ht HT, --host HT     enter your host
  -pt PRT, --prt PRT    enter your port number
  -cr [CRED], --cred [CRED]
                        instead of adding flags you can specify the name of configuration file.
  -v                    add verbose func
```

NOTE: `-u -ht -pt` could be optional since it could be dependant on your privileges on psql software. If they are not working, please talk to your adminstrator if you need change your privileges. `-d` is recommended to make sure you are not inserting new information into some other database. 

NOTE: `--autocommit` is **necessary** if you are at anytime changing ANYTHING (e.g creating/deleting database, creating/truncating tables) in your psql setup. Please double check when you are autocommitting. You could be deleting or manipulating a lot of information. 









