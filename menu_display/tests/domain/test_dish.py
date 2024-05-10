from menu_display.domain.dish.Dish import Dish

def test_dish_model_init():
    dish1 = Dish(1,'Schabowy','Kotlet schabowy z ziemniakami i surówka',5,9.99,'Lunch',['chicken','eggs','butter','potatos','cabbage'],True,'image',None)

    assert dish1.id == 1
    assert dish1.name == 'Schabowy'
    assert dish1.description == 'Kotlet schabowy z ziemniakami i surówka'
    assert dish1.availabilityQty == 5
    assert dish1.price == 9.99
    assert dish1.category == 'Lunch'
    assert dish1.ingredients == ['chicken','eggs','butter','potatos','cabbage']
    assert dish1.active == True
    assert dish1.image == 'image'
    assert dish1.dietaryrestrictions == None