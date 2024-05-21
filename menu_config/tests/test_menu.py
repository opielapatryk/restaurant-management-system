# Built-in modules
from unittest import mock

# Local modules
from main import app
from domain.menu.Menu import Menu

# Third party modules
from fastapi.testclient import TestClient

menu_dict = {
  "_id":"1",
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
	],
  "active": True
}
menu_dict_put = {
  "_id":"1",
  "name":"UPDATED MENU!",
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
	],
  "active": True
}
menu_dict2 = {
  "_id":"2",
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
	],
  "active": True
}

menu = Menu.from_dict(menu_dict)
menu_put = Menu.from_dict(menu_dict_put)
menu2 = Menu.from_dict(menu_dict2)

@mock.patch('main.menu_list_use_case')
def test_list(mock_use_case):
    mock_use_case.return_value = menu

    client = TestClient(app)
    response = client.get('/api/v1/menu')

    response_data = response.json()
    assert response_data == menu_dict
    mock_use_case.assert_called()
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

@mock.patch('main.menu_get_use_case')
def test_get(mock_use_case):
    mock_use_case.return_value = menu

    client = TestClient(app)
    response = client.get('/api/v1/menu/1')

    response_data = response.json()
    assert response_data == menu_dict
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

@mock.patch('main.menu_post_use_case')
def test_post(mock_use_case):
    mock_use_case.return_value = [menu,menu2]

    client = TestClient(app)
    response = client.post('/api/v1/menu/', json=menu_dict2)

    response_data = response.json()
    assert response_data == [menu_dict,menu_dict2]
    
    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"

@mock.patch('main.menu_put_use_case')
def test_put(mock_use_case):
    mock_use_case.return_value = menu_put

    client = TestClient(app)
    response = client.put('/api/v1/menu/1', json=menu_dict_put)

    response_data = response.json()
    assert response_data == menu_dict_put
    
    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"

@mock.patch('main.menu_patch_use_case')
def test_patch(mock_use_case):
    mock_use_case.return_value = menu_put

    client = TestClient(app)
    response = client.patch('/api/v1/menu/1', json=menu_dict_put)

    response_data = response.json()
    assert response_data == menu_dict_put
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"