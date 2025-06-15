from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    


    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

  
    r1 = Restaurant(name="Big Square", address="Moi Avenue, Nairobi")
    r2 = Restaurant(name="Chicken Inn", address="Thika Road Mall, Nairobi")
    r3 = Restaurant(name="Java House", address="Westlands, Nairobi")
    r4 = Restaurant(name="Tuskys Diner", address="Kilimani, Nairobi")
    r5 = Restaurant(name="Mambo Italia", address="Karen, Nairobi")
    db.session.add_all([r1, r2, r3, r4, r5 ])
    db.session.commit()

    p1 = Pizza(name="Nyama Choma Deluxe", ingredients="Grilled Beef, Onions, Tomato")
    p2 = Pizza(name="Kuku BBQ", ingredients="Chicken, BBQ Sauce, Green Pepper")
    p3 = Pizza(name="Pilau Feast", ingredients="Beef Pilau Spices, Onions, Peppers")
    p4 = Pizza(name="Sukuma Supreme", ingredients="Sukuma Wiki, Tomato, Onions, Cheese")
    p5 = Pizza(name="Matoke Madness", ingredients="Matoke, Minced Beef, Cheese")
    db.session.add_all([p1, p2, p3, p4, p5 ])
    db.session.commit()

    rp1 = RestaurantPizza(price=850, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=900, pizza_id=p2.id, restaurant_id=r2.id)
    rp3 = RestaurantPizza(price=950, pizza_id=p3.id, restaurant_id=r3.id)
    rp4 = RestaurantPizza(price=800, pizza_id=p4.id, restaurant_id=r4.id)
    rp5 = RestaurantPizza(price=1000, pizza_id=p5.id, restaurant_id=r5.id)
    db.session.add_all([rp1, rp2, rp3, rp4, rp5 ])
    db.session.commit()

    print("Done seeding")
