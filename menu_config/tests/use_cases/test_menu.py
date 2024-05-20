import pytest
from domain.menu.Menu import Menu
from domain.dish.Dish import Dish
from use_cases.menu_list import menu_list_use_case
from use_cases.menu_get import menu_get_use_case
from unittest import mock

@pytest.fixture
def domain_menu():
    dish1 = Dish(1,"Schabowy","Kotlet schabowy z ziemniakami i surówka",5,9.99,"Lunch",["chicken","eggs","butter","potatos","cabbage"],True,"image",None)
    dish2 = Dish(2, "Pierogi", "Gotowane pierogi ruskie z serem i pieczarkami podane ze śmietaną", 4, 7.50, "Lunch", ["wheat flour", "ricotta cheese", "potatoes", "mushrooms", "onions", "sour cream"], True, "image", None)
    dish3 = Dish(3, "Zupa Żurek", "Żurek na żurku z białą kiełbasą i chlebem", 10, 6.99, "Lunch", ["sour rye flour", "vegetables", "white sausage", "bread", "eggs"], True, "image", None)
    menu = Menu(
        1,"Polish Jadło!","Menu where you can find lot of polish classics from 'kotlet schabowy' to 'zurek'",[dish1,dish2,dish3],True
    )

    return menu

def test_list_menu(domain_menu):
    repo = mock.Mock()
    repo.list.return_value = domain_menu

    result = menu_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_menu

def test_get_menu(domain_menu):
    repo = mock.Mock()
    repo.get.return_value = domain_menu

    result = menu_get_use_case(repo, 1)

    assert result == domain_menu