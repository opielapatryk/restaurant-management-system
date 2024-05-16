from repositories.mongorepo import MongoRepo
from use_cases.menu_list import menu_list_use_case
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the Restaurant API!", "endpoints": {"menu": "api/v1/menu"}}

@app.get("/api/v1/menu")
def menu_list():
    repo = MongoRepo()
    result = menu_list_use_case(repo)
    return result