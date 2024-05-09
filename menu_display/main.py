from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the Restaurant API!", "endpoints": {"dishes": "api/v1/dishes"}}