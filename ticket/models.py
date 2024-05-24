from django.db import models
from django.contrib.auth.models import User


class BusInfo(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bus_no=models.CharField(max_length=10)
    bus_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.bus_no


class Travelinfo(models.Model):
    start_place=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    km=models.IntegerField()
    min_price=models.IntegerField()
    reverse=models.BooleanField(blank=True,default=False)
    bus_no=models.ForeignKey(BusInfo,on_delete=models.CASCADE)


class Stop(models.Model):
    km=models.IntegerField()
    stopname = models.CharField(max_length=100)
    bus_no = models.ForeignKey(Travelinfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.stopname
