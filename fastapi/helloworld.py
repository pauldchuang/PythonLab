from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-world")
async def read_root():
    return {"message": "Hello, World!"}
