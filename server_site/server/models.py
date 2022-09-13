from django.db import models


class Orders(models.Model):
    user_id = models.IntegerField()
    order_info = models.CharField(max_length=255)
