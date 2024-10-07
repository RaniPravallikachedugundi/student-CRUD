from django.db import models
class Train(models.Model):
    Name=models.CharField(max_length=30);
    Train_Number=models.CharField(max_length=20);
    Destination=models.CharField(max_length=30);
    Date=models.CharField(max_length=10);