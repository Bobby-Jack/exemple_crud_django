from django_seed import Seed
from faker import Faker
from .models import Product
import random


def generate_product():
    seeder = Seed.seeder()
    faker = Faker()
    seeder.add_entity(Product, 10, {
        'name' : lambda x : " ".join(faker.words(2)),
        'quantity' : lambda x : random.randint(0, 5),
        'price' : lambda x : round(random.random() * 100, 2 ),
        'color' : lambda x : faker.hex_color()
    })
    print(seeder.execute())