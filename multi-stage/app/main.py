from fastapi import FastAPI
import torch

app=FastAPI()

@app.get("/")
def check():
    return {"Hi! It's my space!"}

@app.get("/name/{name}")
async def read_user(name):
    return {"name":name, "message": "Hi!"}

@app.get("/gpu_check")
async def gpu_check():
    return {"GPU":torch.cuda.is_available()}