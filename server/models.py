

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=True) 

  
    pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Restaurant {self.name}>"


class Pizza(db.Model):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)

    restaurants = db.relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Pizza {self.name}>"


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    pizza = db.relationship('Pizza', back_populates='restaurants')
    restaurant = db.relationship('Restaurant', back_populates='pizzas')

    def __repr__(self):
        return f"<RestaurantPizza Restaurant:{self.restaurant_id} Pizza:{self.pizza_id} Price:{self.price}>"
