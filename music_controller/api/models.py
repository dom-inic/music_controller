from django.db import models
import string 
import random 


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
        
    return code



# Create your models here.

class Room(models.Model):
    code = models.CharField(max_length=8, unique=True, default = "")
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null = False, default=False)
    votes_to_skip = models.IntegerField( null=False, default=1) 
    created_at = models.DateTimeField(  auto_now=True)


# class CarRentalCompany(models.Model):
#     company_name
#     location
#     address 
#     email 
#     phone_no 
#     registration date



# class carsfor companey
#     company id 
#     car photos /


# class rent:
#         company id 
#         owner id 


# class profile: 
#     one to one field. 
#     company/individual 
#     name 
#     location
#     email 
#     phone 
#     date of registration 

