# Local modules
from domain.menu.Menu import Menu
from domain.dish.Dish import Dish

def test_menu_model_init():
    dish1 = Dish(1,"Schabowy","Kotlet schabowy z ziemniakami i surówka",5,9.99,"Lunch",["chicken","eggs","butter","potatos","cabbage"],True,"image",None)
    dish2 = Dish(2, "Pierogi", "Gotowane pierogi ruskie z serem i pieczarkami podane ze śmietaną", 4, 7.50, "Lunch", ["wheat flour", "ricotta cheese", "potatoes", "mushrooms", "onions", "sour cream"], True, "image", None)
    dish3 = Dish(3, "Zupa Żurek", "Żurek na żurku z białą kiełbasą i chlebem", 10, 6.99, "Lunch", ["sour rye flour", "vegetables", "white sausage", "bread", "eggs"], True, "image", None)
    menu = Menu(
        1,"Polish Jadło!","Menu where you can find lot of polish classics from 'kotlet schabowy' to 'zurek'",[dish1,dish2,dish3],True
    )

    assert menu.id == 1
    assert menu.name == "Polish Jadło!"
    assert menu.description == "Menu where you can find lot of polish classics from 'kotlet schabowy' to 'zurek'"
    assert menu.dishes == [dish1,dish2,dish3]
    assert menu.active == True