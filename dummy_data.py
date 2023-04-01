import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
import random
from product.models import *


def seed_brand(n):
    fake=Faker()
    images=['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14jpeg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f"brand/{images[random.randint(1,12)]}"
        )
    print(f"{n} brands seed ")

def seed_product(n):
    fake=Faker()
    images=['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14jpeg']
    FLAG=['New','Feature','Sale']
    TAG=['fruit ','fruits','vegetables',
'healthy',
'food',
'vega',
'healthyfood',
'veggies']

    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            image=f"product_images/{images[random.randint(1,12)]}",
            flag=FLAG[random.randint(0,2)],
            price=round(random.uniform(19.99,199.99),2),
            sku=random.randint(10000,1000000),
            subtitle=fake.text(max_nb_chars=300),
            description=fake.text(max_nb_chars=1000),
            brand=Brand.objects.get(id=random.randint(1,99)),
            tag=TAG[random.randint(0,7)]
        )
    print(f"{n} Products seed ")


def seed_ProductImage(n):
    fake=Faker()
    images=['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14jpeg']
    for _ in range(n):
        ProductImage.objects.create(
            product=Product.objects.get(id=random.randint(1,999)),
            image=f"product_images/{images[random.randint(1,12)]}"
        )
    print(f"{n} Images seed ")


def seed_ProductReview(n):
    fake=Faker()
    for _ in range(n):
        ProductReview.objects.create(
            user=User.objects.get(id=1),
            product=Product.objects.get(id=random.randint(1,999)),
            rate=random.randint(0,5),
            review=fake.text(max_nb_chars=500),
        )
    print(f"{n} Review seed ")



# seed_brand(100)
# seed_product(1000)
# seed_ProductImage(5000)
seed_ProductReview(2000)