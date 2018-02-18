from datetime import datetime
from app import db_instance

########################################################################


class Companyinfo(db_instance.Model):

    # columns : id, ticker, name, marketcap, sector, industry

    __tablename__ = 'companyinfo'
    __table_args__ = {'autoload':True}

    # or we can use a single variable '__table__' to map this table to our table in database schema
    # like this : 
    # __table__ = db.Model.metadata.tables['companyinfo']
    # our way is more informative though


class Histo(db_instance.Model):

    

    __tablename__ = 'histo'
    __table_args__ = {'autoload':True}



