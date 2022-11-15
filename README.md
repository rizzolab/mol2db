# mol2db (UNDER DEVELOPMENT)

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

psycopg is a PostgreSQL python adaptor. This build does not use psycopg2
To install:
```
pip install psycopg
```

psql (PostgreSQL) is a open source object-relational database system
To install:
```
apt-get install postgresql-12
```

## Installation with pyinstaller

To install with pyinstaller:
```
cd mol2db
make mol2db
```

To clean:
```
make clean
```

## Small Tutorial on insert mol2 information into psql

To convert a mol2 file into a `mol2db` compatible csv file.
```
m2db mol2csv -i input.mol2 -o output.csv
```

Then create a new database:
```
m2db --autocommit create DATABASE_NAME
```

Then create psql molecular table:
```
m2db -d DATABASE_NAME -u USER_NAME -pw PASSWORD --ht HOST --pt PORT --autocommit moltables
```

Then insert the .csv file into the table:
```
m2db -d DATABASE_NAME -u USER_NAME -pw PASSWORD --autocommit csv2psql output.csv
```


If you want help:
```
m2db --help
```

output:
```
usage: mol2db [-h] [--autocommit] [-d DBNAME] [-ur USER_NAME] [-pw PW] [-ht HT] [-pt PRT]
              {mol2csv,csv2mol2,execute,csv2psql,moltables,create,delete} ...

positional arguments:
  {mol2csv,csv2mol2,execute,csv2psql,moltables,create,delete}
                        help for subcommand
    mol2csv             to convert molecules into csv
    csv2mol2            to convert csv file into mol2 file
    execute             to execute a sql string
    csv2psql            to load up csv into db
    moltables           to create a molecular table
    create              to create your own db. This command will initially connect db
                        named "postgres" under your username. This should be created by
                        default when installing psql. Then it will create the dbname of
                        your choice. Please do not delete or change that name
    delete              to delete your own db. This command will initially connect db
                        named "postgres" under your username. This should be created by
                        default when installing psql. Then it will create the dbname of
                        your choice. Please do not delete or change that name

optional arguments:
  -h, --help            show this help message and exit
  --autocommit          specify if you want to autocommit(True) or not(False). No flag
                        (False)
  -d DBNAME, --dbname DBNAME
                        enter your database name to access
  -ur USER_NAME, --user USER_NAME
                        enter your user name
  -pw PW, --pw PW       enter your password
  -ht HT, --host HT     enter your host
  -pt PRT, --prt PRT    enter your port number

```

NOTE: `-u -pw -ht -pt` could be optional since it could be dependant on your privileges on psql software. If they are not working, please talk to your adminstrator if you need change your privileges. `-d` is recommended to make sure you are not inserting new information into some other database. 

NOTE: `--autocommit` is **necessary** if you are at anytime changing ANYTHING (e.g creating/deleting database, creating/truncating tables) in your psql setup. Please double check when you are autocommitting. You could be deleting or manipulating a lot of information. 





