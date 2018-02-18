
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




