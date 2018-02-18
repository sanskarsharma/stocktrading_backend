import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-easily-guess'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql.2996@localhost/growthplug'
    #os.environ.get("DATABASE_URL") or \
	#'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False