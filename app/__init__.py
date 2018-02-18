from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app_instance = Flask(__name__)

app_instance.config.from_object(Config)

db_instance = SQLAlchemy(app_instance)
db_instance.Model.metadata.reflect(db_instance.engine)  # VvvvvvIMP line 
# ... it syncs our tables(in models.py or anywhere else) with the actual tables of database schema, on startup


migrate = Migrate(app_instance,db_instance)


###############################################################################################################

# This code also works but it is more directed towards sqlalchemy in general, we are using flask_sqlalchemy 
# flask_sqlalchemy is a wrapper around the supersexy orm that sqlalchemy is.
# we have found an more direct way of doing things* via flask_sqlalchemy so we don't need sqlalchemy to save our ass here.
# thanks to this answer on SO : https://stackoverflow.com/a/19064993

# *doing things : conecting an already created database schema with our flask app

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#from sqlalchemy import create_engine


# #engine =  create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
# #Base = declarative_base(engine)

# # def loadSession():
# #     """"""
# #     metadata = Base.metadata
# #     Session = sessionmaker(bind=engine)
# #     session = Session()
# #     return session


# # print("hiiiiiiiiiii")

# # #session = None
# # #print("helooooooooo")
# # session = loadSession()
# # # res = session.query(Companyinfo).all()
# # # print (res[1].name)

##################################################################################################################


from app import routes, models
