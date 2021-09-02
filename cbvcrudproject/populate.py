import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cbvcrudproject.settings')
import django
django.setup()

from testapp.models import Company
from faker import Faker
fake = Faker()
def populate(n):
    for i in range(n):
        fname = fake.company()
        flocation = fake.city()
        fceo = fake.name()
        company_record = Company.objects.get_or_create(name=fname,location=flocation,ceo=fceo)
populate(10)