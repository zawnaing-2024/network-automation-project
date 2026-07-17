from sqlalchemy import create_engine, Column, Integer, String , DateTime
from sqlalchemy.sql import func
from .database import Base

class Device(Base):
    __tablename__= 'devices'

    id = Column(Integer, primary_key=True, index=True)
    hostname= Column(String, index=True)
    ip_address = Column(String, unique = True, nullable= False) 
    vendor = Column(String)
    model = Column(String)
    location = Column(String)
    os_version = Column(String)
    management_interface =  Column(String)
    serial_number = Column(String)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())



class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String,index=True)
    email= Column(String, unique = True ,nullable= False)
    password=Column(String)