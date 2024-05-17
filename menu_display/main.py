from repositories.mongorepo import MongoRepo
from use_cases.menu_list import menu_list_use_case
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the Restaurant API!", "endpoints": {"menu": "api/v1/menu"}}

@app.get("/api/v1/menu")
def menu_list(name:str=None):
    repo = MongoRepo()
    result = menu_list_use_case(repo)

    if name:
        result = filter(lambda m: m['name'] == name, result)
    
    return result