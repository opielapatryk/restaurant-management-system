import pymongo
import pytest

@pytest.fixture(scope="session")
def mg_database_empty():
    client = pymongo.MongoClient(
        host='localhost',
        port=27017,
        username='root',
        password='mongodb',
    )
    db = client['menu_display']

    yield db

    client.drop_database('menu_display')
    client.close()


@pytest.fixture(scope="function")
def mg_test_data():
    return {
  "name":"Polish Jadło!",
  "description":"Menu where you can find lot of polish classics from kotlet schabowy to zurek",
  "dishes":[
    {
      "id":1,"name":"Schabowy","description":"Kotlet schabowy z ziemniakami i surówka","availabilityQty":5,"price":9.99,"category":"Lunch","ingredients":["chicken","eggs","butter","potatos","cabbage"],"active":True,"image":"image","dietaryrestrictions":None
    },
		{
      "id":2, "name":"Pierogi", "description":"Gotowane pierogi ruskie z serem i pieczarkami podane ze śmietaną", "availabilityQty":4, "price":7.50, "category":"Lunch", "ingredients":["wheat flour", "ricotta cheese", "potatoes", "mushrooms", "onions", "sour cream"], "active":True, "image":"image", "dietaryrestrictions":None
    },
		{
      "id":3, "name":"Zupa Żurek", "description":"Żurek na żurku z białą kiełbasą i chlebem", "availabilityQty":10, "price":6.99, "category":"Lunch", "ingredients":["sour rye flour","vegetables", "white sausage", "bread", "eggs"], "active":True, "image":"image", "dietaryrestrictions":None
    }
	]
}


@pytest.fixture(scope="function")
def mg_database(mg_database_empty, mg_test_data):
    collection = mg_database_empty.menu

    collection.insert_one(mg_test_data)

    yield mg_database_empty

    collection.delete_one({})