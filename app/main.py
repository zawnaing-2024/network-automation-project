from fastapi import FastAPI

app = FastAPI (
    title = "Network Automation Platform",
    version = "0.1"
)

@app.get("/")
def home():
    return {
        "message" : "Welcome to Network Automation Platform"
    }