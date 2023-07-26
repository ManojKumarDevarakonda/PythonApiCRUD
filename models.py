from sqlalchemy import *
from sqlalchemy.sql import *
from database import Base
from database import dbschema



class Uploads(Base) :
    __tablename__ = "uploads"
    __table_args__ = {'schema': dbschema}
    UploadId = Column(Integer, primary_key=True,autoincrement=True)
    UserId = Column(Integer)
    Title = Column(String)
    Body = Column(String)
    Timestamp = Column(String)

    
