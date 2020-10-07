from django.db import models
from django.core.validators import MinValueValidator, \
    MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50,
                            unique=True)  # users coupon code
    valid_from = models.DateField()  # coupon valid date
    valid_to = models.DateField()  # coupon expire date
    discount = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(100)])  # discount rate 0 - 100
    active = models.BooleanField()  # indication the coupon is valid

    def __str__(self):
        return self.code

# Create your models here.
