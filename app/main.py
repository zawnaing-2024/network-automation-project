from fastapi import FastAPI

app = FastAPI (
    title = "Network Automation Platform",
    version = "0.2"
)

devices = []
@app.get("/")
def home():
    return {
        "message" : "Welcome to Network Automation Platform"
    }


@app.get("/devices")
def get_devices():
    return devices


@app.post("/devices")

def add_devices(device:dict):
    devices.append(device)

    return {
        "status": "success",
        "device": device
    }