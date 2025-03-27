from fastapi import FastAPI
from time import sleep

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/slow")
def slow_endpoint():
    sleep(1)  # Simulate some delay
    return {"message": "This is a slow response"}
