from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY=(
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)
class Profile(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=20, null=True)
    image=models.ImageField(default ='avater.jpg',upload_to='Profile_Images')
        
    
    def __str__(self):
        return f'{self.staff.username}-Profile'
  

    
