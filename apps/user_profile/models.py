from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from apps.orders.countries import Countries

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addres_line_1 = models.CharField(max_length=255, default='')
    addres_line_2 = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    state_province_region = models.CharField(max_length=255, default='')
    zipcode = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=255, default='')
    country_region = models.CharField(
        max_length=255, choices=Countries.choices, default=Countries.Canada)

    def __str__(self):
        return self.user