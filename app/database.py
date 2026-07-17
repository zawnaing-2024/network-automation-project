from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ဤဖိုင်တွင် Column, Integer တို့ မလိုပါ။




#class Device(Base):
 #   __tablename__= 'devices'
  #  id = Column (Integer,primary_key=True)
   # name = Column(String)                  
    #device_type = Column(String)           
    #ip_address = Column(String)


DATABASE_URL = "postgresql://network_user:1Netw0rk%402026@localhost/network_inventory"
engine = create_engine(DATABASE_URL)
#Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()
