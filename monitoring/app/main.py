from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from prometheus_fastapi_instrumentator import Instrumentator

app=FastAPI()

@app.get("/")
def check():
    return {"Hi! It's my space!"}

@app.get("/{name}")
async def read_user(name):
    default = os.environ['NUM']
    return {"name":name, "message": f"Hi! {name}, {default}"}

Instrumentator().instrument(app).expose(app)