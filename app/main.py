from fastapi import FastAPI, Depends
from . import models,schemas
from sqlalchemy.orm import Session
from .database import engine,SessionLocal
from fastapi import HTTPException

app = FastAPI (
    title = "Network Automation Platform",
    version = "0.4"
)

models.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {
        "message" : "Welcome to Network Automation Platform"
    }





@app.post("/devices", response_model=schemas.DeviceResponse)

def create_device(device: schemas.DeviceCreate , db : Session = Depends(get_db)):
    device_data = device.dict()
    device_data['ip_address'] = str(device_data['ip_address'])
    new_device = models.Device(**device_data)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

@app.get("/devices")
def read_devices(db: Session = Depends(get_db)):
    devices = db.query(models.Device).all()
    return devices


@app.post("/users")

def create_user(user: schemas.UserCreate , db : Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message" : "User added Done",
        "User_Data" : new_user
    }

@app.put("/devices/{device_id}" , response_model= schemas.DeviceResponse)
def update_device_full(device_id:int,device: schemas.DeviceCreate,db: Session = Depends(get_db)):
    db_device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if not db_device:
        raise HTTPException(status_code=404 , detail ="Device not found")

    update_data = device.model_dump(mode='json')
    for key,value in update_data.items():
        setattr(db_device,key,value)

    db.commit()
    db.refresh(db_device)
    return db_device


@app.patch("/devices/{device_id}" , response_model=schemas.DeviceResponse)
def update_device_partial(device_id:int , device_update: schemas.DeviceUpdate ,db: Session = Depends(get_db)):
    db_device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if not db_device:
        raise HTTPException (status_code=404, detail="Device Not Found")

    update_data = device_update.model_dump(exclude_unset=True,mode="json")

    for key,value in update_data.items():
        setattr(db_device,key,value)

    db.commit()
    db.refresh(db_device)
    return db_device

@app.delete("/devices/{device_id}")
def delete_device(device_id:int , db: Session = Depends(get_db)):
    db_device = db.query(models.Device).filter(models.Device.id==device_id).first()

    if not db_device:
        raise HTTPException (status_code = 404 , detail = "Device Not Found")

    db.delete(db_device)
    db.commit()
    return {
        "message" : f"Device ID {device_id} have been deleted successfully."}

@app.get("/users")
def read_users(db : Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users