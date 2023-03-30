class Customer:

    def __init__(self, first_name, last_name):
        self._reviews = []
        if not 1 <= len(first_name) <= 25:
            raise ValueError("First name must be between 1 and 25 characters")
        if not 1 <= len(last_name) <= 25:            
            raise ValueError("Last name must be between 1 and 25 characters")
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not 1 <= len(value) <= 25:
            raise ValueError("First name must be between 1 and 25 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not 1 <= len(value) <= 25:
            raise ValueError("Last name must be between 1 and 25 characters")
        self._last_name = value

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def restaurants(self):
        return list({review.restaurant for review in self._reviews})
    
    @property
    def reviews(self):
        return self._reviews

    def get_num_reviews(self):
        return len(self._reviews)

    def add_review(self, review):
        self._reviews.append(review)

    def create_review(self, restaurant, rating):
        # This prevents a circular import!
        from classes.review import Review
        review = Review(self, restaurant, rating)
        return review