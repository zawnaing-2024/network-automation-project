from fastapi import FastAPI
from .models import Device

app = FastAPI (
    title = "Network Automation Platform",
    version = "0.3"
)

devices: list[Device]=[]

@app.get("/")
def home():
    return {
        "message" : "Welcome to Network Automation Platform"
    }


@app.get("/devices")
def get_devices() :
    return devices


@app.post("/devices")

def add_device(device:Device):
    devices.append(device)

    return {
        "status": "success",
        "device": device
    }