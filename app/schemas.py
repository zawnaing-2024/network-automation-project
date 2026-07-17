from pydantic import BaseModel,IPvAnyAddress
from ipaddress import IPv4Address
from datetime import datetime
from typing import Optional

class DeviceCreate(BaseModel):
    hostname : str
    ip_address : IPv4Address
    vendor : str
    model : str
    location : str
    os_version : str
    management_interface : str
    serial_number : str

class DeviceResponse(BaseModel):
    hostname : str
    ip_address : IPv4Address
    vendor : str
    model : str
    location : str
    os_version : str
    management_interface : str
    serial_number : str

    created_at : datetime
    updated_at: datetime

    
    class Config:
        rom_attributes = True

class DeviceUpdate(BaseModel):
    hostname : Optional[str] = None
    ip_address : Optional[IPv4Address]= None
    vendor : Optional[str] = None
    model : Optional[str] = None
    location : Optional[str] = None
    os_version : Optional[str] = None
    management_interface : Optional[str] = None
    serial_number : Optional[str] = None

class UserCreate(BaseModel):
    name: str
    email : str
    password : str