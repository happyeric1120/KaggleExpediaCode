from sqlalchemy import *
from  sqlalchemy.ext.declarative  import  declarative_base
Base  =  declarative_base()

class SearchID(Base):
    """This class maps to [DataAnalytics].[srchIds]"""
    
    __tablename__ = 'srchIds'

    srch_id = Column('srch_id', Integer, primary_key=True)

    def __init__(self, srch_id):
        self.srch_id = srch_id

    def __repr__(self):
        return "<SearchID(%d)>" % (self.srch_id)

