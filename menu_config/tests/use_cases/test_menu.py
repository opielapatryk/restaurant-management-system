# Third party modules
import pytest

# Local modules
from domain.menu.Menu import Menu
from domain.dish.Dish import Dish
from use_cases.menu_list import menu_list_use_case
from use_cases.menu_get import menu_get_use_case
from use_cases.menu_post import menu_post_use_case
from use_cases.menu_put import menu_put_use_case
from use_cases.menu_patch import menu_patch_use_case
from use_cases.menu_delete import menu_delete_use_case

# Built-in modules
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

@pytest.fixture
def domain_menu2():
    dish1 = Dish(1,"Schabowy","Kotlet schabowy z ziemniakami i surówka",5,9.99,"Lunch",["chicken","eggs","butter","potatos","cabbage"],True,"image",None)
    dish2 = Dish(2, "Pierogi", "Gotowane pierogi ruskie z serem i pieczarkami podane ze śmietaną", 4, 7.50, "Lunch", ["wheat flour", "ricotta cheese", "potatoes", "mushrooms", "onions", "sour cream"], True, "image", None)
    dish3 = Dish(3, "Zupa Żurek", "Żurek na żurku z białą kiełbasą i chlebem", 10, 6.99, "Lunch", ["sour rye flour", "vegetables", "white sausage", "bread", "eggs"], True, "image", None)
    menu2 = Menu(
        2,"Polish Jadło!","Menu where you can find lot of polish classics from 'kotlet schabowy' to 'zurek'",[dish1,dish2,dish3],True
    )

    return menu2

@pytest.fixture
def domain_menu_post():
    dish1 = Dish(1,"Schabowy","Kotlet schabowy z ziemniakami i surówka",5,9.99,"Lunch",["chicken","eggs","butter","potatos","cabbage"],True,"image",None)
    dish2 = Dish(2, "Pierogi", "Gotowane pierogi ruskie z serem i pieczarkami podane ze śmietaną", 4, 7.50, "Lunch", ["wheat flour", "ricotta cheese", "potatoes", "mushrooms", "onions", "sour cream"], True, "image", None)
    dish3 = Dish(3, "Zupa Żurek", "Żurek na żurku z białą kiełbasą i chlebem", 10, 6.99, "Lunch", ["sour rye flour", "vegetables", "white sausage", "bread", "eggs"], True, "image", None)
    menu = Menu(
        1,"Polish Jadło!","Menu where you can find lot of polish classics from 'kotlet schabowy' to 'zurek'",[dish1,dish2,dish3],True
    )
    menu2 = Menu(
        2,"Polish Jadło!","Menu where you can find lot of polish classics from 'kotlet schabowy' to 'zurek'",[dish1,dish2,dish3],True
    )

    return [menu,menu2]

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

def test_post_menu(domain_menu_post,domain_menu2):
    repo = mock.Mock()
    repo.post.return_value = domain_menu_post

    result = menu_post_use_case(repo, domain_menu2)

    assert result == domain_menu_post

def test_put_menu(domain_menu,domain_menu2):
    repo = mock.Mock()
    repo.put.return_value = domain_menu2

    result = menu_put_use_case(repo, domain_menu2, 1)

    assert result == domain_menu2

def test_patch_menu(domain_menu,domain_menu2):
    repo = mock.Mock()
    repo.patch.return_value = domain_menu2

    result = menu_patch_use_case(repo, domain_menu2, 1)

    assert result == domain_menu2

def test_delete_menu(domain_menu,domain_menu2):
    repo = mock.Mock()
    repo.delete.return_value = domain_menu2

    result = menu_delete_use_case(repo, 1)

    repo.delete.assert_called_with(1)
    assert result == domain_menu2