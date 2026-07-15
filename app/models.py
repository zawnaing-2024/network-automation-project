from pydantic import BaseModel ,  IPvAnyAddress, ValidationError
from ipaddress import IPv4Address

class Device(BaseModel):
    hostname : str
    ip : IPv4Address
    vendor : str
    model : str
    location : str
    os_version : str
    management_interface : str
    serial_number : str
