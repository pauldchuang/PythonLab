from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-world")
async def get_helloworld():
    return {"message":"Hello,World!"}
