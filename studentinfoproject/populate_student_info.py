import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfoproject.settings')
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake = Faker()

def phone_no():
    num = randint(6,9)
    num1 = str(num)
    for i in range(9):
        num1 = num1 + str(randint(0,9))
    return int(num1)

def populate(n):
    for i in range(n):
        frollno = randint(1,100)
        fname = fake.name()
        fdob = fake.date()
        femail = fake.email()
        fphoneno = phone_no()
        faddress = fake.address()
        fmark = randint(1,100)
        student_record = Student.objects.get_or_create(rollno = frollno,name = fname,dob = fdob,email = femail,mark = fmark,phoneno = fphoneno,address = faddress)
populate(60)