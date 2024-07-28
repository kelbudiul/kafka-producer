from faker import Faker
import random
import time

fake = Faker()

def generate_event():
    """
    Generate a random e-commerce event.
    """
    return {
        'user_id': fake.uuid4(),  # Generate a random UUID for user ID
        'timestamp': int(time.time()),  # Current timestamp
        'product_id': fake.uuid4(),  # Generate a random UUID for product ID
        'category': random.choice(['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Toys']),  # Random category
        'price': round(random.uniform(10, 1000), 2),  # Random price between 10 and 1000
        'quantity': random.randint(1, 5),  # Random quantity between 1 and 5
        'is_purchase': random.choice([True, False])  # Randomly decide if it's a purchase or not
    }