# Swiss-Tournament
Created by: Noah Shmais
Date: 3/31/2017

Swiss-system tournament is a non-eliminating tournament format which features a set number of rounds of competition

## Files

The project contain of three files:
 ```
   1.tournament.py
   2.tournament.sql
   3.tournament_test.py
```

- The First file (tournament.py) contain the code for the swiss tournament (sql and python) for each function
- The Second file (tournament.sql) contain the database tables for the tournament
- The Third file (tournament_test.py) contain the test_cases of the code.

## Install

To run database (tournament) on vagrant: 
1. run (psql) in the command line to check if you proparly installed psql

 ```javascript
    $psql
```

2. you can run tournament.psql by running (\i tournament.sql) in the command line 

 ```javascript
    \i tournament.sql
```

3. run  (psql -d tournament) in command line to log in to the desired database
 ```javascript
    psql -d tournament
```

4. you can create and/or drop tables or the entire database using sql
5. you can check select, update, insert,... to the created database
6. (Ctrl+d) will log_off and return you to your VM    
 


## License

`Swiss-Tournament` is a public domain work, dedicated using feel free to do whatever you want with it.
