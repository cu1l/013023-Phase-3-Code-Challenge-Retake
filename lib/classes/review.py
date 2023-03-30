from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be of type Customer")
        if not isinstance(restaurant, Restaurant):
            raise Exception("Restaurant must be of type Restaurant")
        if not 1 <= rating <= 5:
            raise Exception("Rating must be a number between 1 and 5, inclusive")
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

        customer.add_review(self)
        restaurant.add_review(self)


    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be of type customer")
        self._customer = value
 
    @property
    def restaurant(self):
        return self._restaurant

    @restaurant.setter
    def restaurant(self, value):
        if not isinstance(restaurant, Restaurant):
            raise Exception("Restaurant must be of type restaurant")
        self._restaurant = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not 1 <= value <= 5:
            raise Exception("Rating must be a number between 1 and 5")
        self._rating = value

    

