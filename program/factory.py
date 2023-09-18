import random

def generate_random_book_data():
    title = "Book " + str(random.randint(1, 1000))
    price = round(random.uniform(10.0, 100.0), 2)
    return title, price