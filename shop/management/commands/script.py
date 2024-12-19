from django.core.management import BaseCommand
from shop.models import Item,Category,Tag,Image
from django.contrib.contenttypes.models import ContentType
from faker import Faker
import time
from django.db import transaction





faker = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        categories = Category.objects.all()
        item_objects = Item.objects.all()[:5]
        for category in categories:
            category.items.add(*item_objects)


        # with transaction.atomic():
            # category = Category.objects.create(name='For blacks')
            # item = Item.objects.create(name='KFC', category=category)



        # Category.objects.filter(id__gt=500).delete()


        # start = time.time()
        # for _ in range(1000):
        #     category = Category.objects.create(name=faker.word())

        # end = time.time()
        # print(end-start)

        # categories = []
        # start = time.time()
        # for _ in range(1000):   
        #     category = Category(name=faker.word())
        #     categories.append(category)
        # Category.objects.bulk_create(categories)
        # end = time.time()
        # print(end-start)



        # category = Category(name='toys', description='about toys')
        # category.save()

        # category = Category.objects.create(name='cars')


        # categories = Category.objects.filter(id__gt=500)
        # to_update = []

        # for category in categories:
        #     category.name = faker.name()
        #     to_update.append(category)
        
        # Category.objects.bulk_update(to_update, fields=['name'])





