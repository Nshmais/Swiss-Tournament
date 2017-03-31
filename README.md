# Swiss-Tournament
created by: Noah Shmais
date: 3/31/2017

Swiss-system tournament is a non-eliminating tournament format which features a set number of rounds of competition


the project contain of three files 
1.tournament.py
2.tournament.sql
3.tournament_test.py


- The First file (tournament.py) contain the code for the swiss tournament (sql and python) for each function
- The Second file (tournament.sql) contain the database tables for the tournament
- The Third file (tournament_test.py) contain the test_case of the code.


To run database (tournament) on vagrant: 
1. run (psql) in the command line to check if you proparly installed psql
2. you can run tournament.psql by running (\i tournament.sql) in the command line 
3. run  (psql -d tournament) in command line to log in to the desired database
4. you can create and/or drop tables or the entire database using sql
5. you can check select, update, insert,... to the created database
6. (Ctrl+d) will log_off and return you to your VM    
 
