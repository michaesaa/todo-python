from fastapi import FastAPI

app = FastAPI()

@app

def root():
    return "hola fastapi"