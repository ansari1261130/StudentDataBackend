from django.db import models

# Choices for gender field
GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
]

class StudentData(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=10)  
    email = models.EmailField(max_length=200)  
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Others')  

    def __str__(self):
        return self.name 
