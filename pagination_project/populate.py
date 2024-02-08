import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pagination_project.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *

fake = Faker()

def populate(n):
    for i in range(n):
        feno = randint(101,500)
        fename = fake.name()
        fesal = randint(10000,25000)
        feaddr = fake.city()
        emp_record = Employee.objects.get_or_create(
        eno = feno,
        ename = fename,
        esal = fesal,
        eaddr = feaddr
        )
n = int(input('Enter no.of recordes to enter :'))
populate(n)
print(f'{n} inserted successfully...!!')
