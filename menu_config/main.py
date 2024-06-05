# Local modules
from repositories.mongorepo import MongoRepo
from use_cases.menu_list import menu_list_use_case
from use_cases.menu_get import menu_get_use_case
from use_cases.menu_post import menu_post_use_case
from use_cases.menu_put import menu_put_use_case
from use_cases.menu_patch import menu_patch_use_case
from use_cases.menu_delete import menu_delete_use_case
from use_cases.producer import ProducerService
from repositories.rabbitmq import RabbitMQProducer
from client import AuthClient
from domain.auth.auth import AuthData
from domain.auth.token import TokenData

# Third party modules
from fastapi import FastAPI, status, HTTPException, Depends

app = FastAPI(
    docs_url="/api/v1/config/docs", openapi_url="/api/v1/config/openapi.json"
)
auth_client = AuthClient()


# Auth
@app.post("/login")
def login(auth_data: AuthData):
    response = auth_client.authenticate(auth_data.email, auth_data.password)
    if not response.success:
        raise HTTPException(status_code=401, detail=response.message)
    return {
        "access_token": response.access_token,
        "refresh_token": response.refresh_token,
    }


# To use on the client side by catching 401 error
@app.post("/refresh-token")
def refresh_token(token_data: TokenData):
    response = auth_client.refresh_token(token_data.token)
    if not response.success:
        raise HTTPException(status_code=401, detail=response.message)
    return {
        "access_token": response.access_token,
        "refresh_token": response.refresh_token,
    }


def verify_token(token_data: TokenData):
    response = auth_client.verify_token(token_data.token)
    if not response.valid:
        raise HTTPException(status_code=401, detail=response.message)
    return {"message": response.message}


# RabbitMQ
def produce_message(
    message,
    service: ProducerService = ProducerService,
    broker: RabbitMQProducer = RabbitMQProducer,
):
    try:
        service(broker).send_message(message)
        return {"status": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""


# API
@app.get(
    "/api/v1/config",
    status_code=status.HTTP_200_OK,
    name="get_menu",
)
def get_menu(token: TokenData = Depends(verify_token)):
    try:
        repo = MongoRepo()
        menu = menu_list_use_case(repo)

        return menu

    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found!"
        )


@app.get(
    "/api/v1/config/{id}",
    status_code=status.HTTP_200_OK,
    name="get_menu",
)
def get_menu_by_id(id, token: TokenData = Depends(verify_token)):
    try:
        repo = MongoRepo()
        menu = menu_get_use_case(repo, id)

        return menu

    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found!"
        )


@app.post(
    "/api/v1/config/",
    status_code=status.HTTP_201_CREATED,
    name="post_menu",
)
def post_menu(menu: dict, token: TokenData = Depends(verify_token)):
    repo = MongoRepo()

    try:
        result = menu_post_use_case(repo, menu)

        if menu.get("active") == True:
            produce_message(result)

        return result
    except:
        raise HTTPException(
            status_code=400,
            detail="Menu already exists or missing required fields",
        )


@app.put(
    "/api/v1/config/{id}",
    status_code=status.HTTP_201_CREATED,
    name="put_menu",
)
def put_menu(menu: dict, id, token: TokenData = Depends(verify_token)):
    repo = MongoRepo()

    try:
        result = menu_put_use_case(repo, menu, id)

        if menu.get("active") == True:
            produce_message(result)

        return result
    except:
        raise HTTPException(status_code=400, detail="Failed to update menu")


@app.patch(
    "/api/v1/config/{id}",
    status_code=status.HTTP_200_OK,
    name="patch_menu",
)
def patch_menu(
    menu_fields: dict, id, token: TokenData = Depends(verify_token)
):
    repo = MongoRepo()

    try:
        result = menu_patch_use_case(repo, menu_fields, id)

        menu_active = menu_get_use_case(repo, id)["active"]

        if menu_active == True:
            produce_message(result)

        return result
    except:
        raise HTTPException(status_code=400, detail="Failed to update menu")


@app.delete(
    "/api/v1/config/{id}",
    status_code=status.HTTP_200_OK,
    name="delete_menu",
)
def delete_menu(id, token: TokenData = Depends(verify_token)):
    repo = MongoRepo()

    try:
        result = menu_delete_use_case(repo, id)
        return result
    except:
        raise HTTPException(status_code=400, detail="Failed to delete menu")
