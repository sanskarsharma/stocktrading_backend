
*learned data handling, using pre-defined db schema for flask apps via SQLAlchemy, REST api calls

#########___Install Notes____##########

virtualenvironment folder is excluded from git repo
using command : echo folder_name >> .gitignore

requirements.txt is added/updated using : pip freeze > requirements.txt
ALWAYS UPDATE requirements.txt WHENEVER YOU COMMIT, ALWAYS.

Note:
virtualenvironment is not added to git, create one where you clone this project.
In this repo, the virtual environment folder is already added to .gitignore file so to carry on this legacy of not including virtualenvironment in git repo,
just name your new virtualenvironment as "virtualenv" as this folder name is already added to .gitignore

to make a virtualenvironment use command : python -m venv <virtual_env_name>
then to install all dependencies : 
1) activate your venv
2) pip install -r requirements.txt


# database and migrations
1st migration - flask db init
flask db migrate -m "migration message"
flask db upgrade

IMP NOTE - if using predefined schema like the one in this proj, do every schema alteration/updation from mysql server only and not through migrations/models.py . REASON - causes issue on run, active bug in sql-alchemy(https://github.com/mitsuhiko/flask-sqlalchemy/pull/222).
So the approch is - stick to one-way approach with the db, for now.
I have deleted the alembic table and migrations folder for this proj to make things smooth.

###############____Setup Notes____################

# putting csv data into mysql db 

csv,xlsx data handling saved in ipython notebook 

commands from SO and other useful links - kept in bookmarks under "stocktrade_growthplug" folder

#### database "growthplug" in mysql server
#### table companyinfo
mysql> create table companyinfo (id INTEGER PRIMARY KEY,ticker TEXT,name TEXT,marketcap TEXT,sector TEXT,industry TEXT);
Query OK, 0 rows affected (2.95 sec)

mysql> load data local infile 'prices763fefc.csv' into table histo fields terminated by ',' lines termimysql> load data local infile 'stocksinfo.csv' into table companyinfo fields terminated by ',' lines terminated by '\n' (id,ticker,name,marketcap,sector,industry);
Query OK, 3169 rows affected, 1482 warnings (1.26 sec)
Records: 3169  Deleted: 0  Skipped: 0  Warnings: 1482

#### table histo
mysql> create table histo (id INTEGER PRIMARY KEY, date TEXT,symbol TEXT,open TEXT,close TEXT,low TEXT,high TEXT,volume TEXT);
Query OK, 0 rows affected (0.67 sec)

mysql> load data local infile 'histodataforindex.csv' into table histo fields terminated by ',' lines terminated by '\n' (id,date,symbol,open,close,low,high,volume);
Query OK, 851263 rows affected, 2 warnings (27.33 sec)
Records: 851264  Deleted: 0  Skipped: 1  Warnings: 2




