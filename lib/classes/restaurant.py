from classes.customer import Customer
class Restaurant:
    all = []

    def __init__(self, name):
        self._reviews = []
        self._customers = []
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def reviews(self):
        return self._reviews

    @property
    def customers(self):
        for review in self._reviews:
            if review.customer not in self._customers:
                self._customers.append(review.customer)
        return self._customers
    
    def add_review(self, review):
        self._reviews.append(review)

    def average_star_rating(self):
        return sum(list(map(lambda review: review.rating, self._reviews)))/len(self._reviews)

    def restaurants(self):
        return list({review.restaurant for review in self._reviews})

    @classmethod
    def get_all_restaurants(cls):
        restaurant_list = []
        for restaurant in cls.all:
            if restaurant not in restaurant_list:
                restaurant_list.append(restaurant)
        return restaurant_list