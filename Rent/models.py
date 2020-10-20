from django.db import models

from django.contrib.auth.models import User

class Executive(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    mobile  = models.CharField(max_length=13)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

class Agreement(models.Model):
    agreementid= models.CharField(unique=True,max_length=30)
    name= models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    monthrent= models.PositiveIntegerField(null=False)
    hownername = models.CharField(max_length=100)
    contractperiod = models.PositiveIntegerField(blank=False)
    startdate= models.DateField()
    status =models.BooleanField(default=False)
    increment = models.PositiveIntegerField(default=False)
    incrementamount = models.PositiveIntegerField(default=False)
    incrementstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Rent(models.Model):
    agreementid = models.CharField(max_length=30)
    btsid = models.PositiveIntegerField(null=True)
    btsname = models.CharField(max_length=100)
    todate = models.DateField(null=False)
    monthrent = models.PositiveIntegerField(default=False)
    totalmonth = models.PositiveIntegerField(blank=True,null=True)
    rentexcludingincrement = models.PositiveIntegerField(default=False)
    totalrent =models.PositiveIntegerField(blank=True,null=True)
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    hownername = models.CharField(max_length=100)
    contractperiod = models.PositiveIntegerField(default=False)
    monthincrement = models.PositiveIntegerField(default=False)
    incrementamount = models.PositiveIntegerField(default=False)
    checkstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.btsname




