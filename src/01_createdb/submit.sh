#!/bin/bash
#This is a bash script that creates a database with a name as an argument


#this is where we assign a name of the database in to `db_name`
db_name=$1



#this creates the db with the variable `db_name`
createdb ${db_name}




psql -l
