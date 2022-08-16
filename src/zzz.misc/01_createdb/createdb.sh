#!/bin/bash
#This is a bash script that creates a database with a name as an argument

check_db_name_exist(){

    if [[ ! -z `psql -Atqc '\list '"$1" postgres` ]]
    then
        return 0 
    else
        return 1
    fi
}

#this creates the db with the variable `db_name`
while read db_name
do 
    if (! check_db_name_exist ${db_name})
    then 
        createdb ${db_name}
        echo "${db_name} db created"
    else 
#if the db name exist, create a new dbname where it will be prepedned with a numerical tag
        echo "${db_name} name already taken."
        for num in {1..5}
        do 
            new_db_name=${db_name}_${num}
            if (check_db_name_exist ${new_db_name})
            then
                echo "${new_db_name} name already taken."
                continue
            else
                createdb ${new_db_name} 
                echo "Created a new database name with prepended numeral tag: ${new_db_name}"
                break
            fi
        done
    fi

done < "db_name.txt"
