from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from searchid import SearchID

mssqlDsn = 'SQL Server 2012'
dbUser = 'ExternalConnTester'
dbPwd = 'gz3000gz3000'
dbName = 'DataAnalytics'

engine = create_engine('mssql+pyodbc://%s:%s@localhost/%s' % (dbUser, dbPwd, dbName))
engine.echo = True

Session = sessionmaker(bind=engine)
session = Session()

for searchId in session.query(SearchID).yield_per(1):
    print(searchId.srch_id)
