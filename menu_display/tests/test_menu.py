from unittest import mock
from fastapi.testclient import TestClient
from main import app
from domain.menu.Menu import Menu

menu_dict = {
  "id":1,
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