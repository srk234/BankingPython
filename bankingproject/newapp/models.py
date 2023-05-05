from django.db import models
# Create your models here.

ACCOUNT = (
    ('','Select an account type'),
    ('Current','Current'),
    ('Savings','Savings')
)


class District(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account = models.CharField(max_length=50, null=True, choices=ACCOUNT)
    CreditCard = models.BooleanField(default=False)
    DebitCard = models.BooleanField(default=False)
    ChequeBook = models.BooleanField(default=False)


    def __str__(self):
        return self.name