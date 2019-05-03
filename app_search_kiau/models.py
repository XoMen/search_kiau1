from django.db import models


class post(models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=25 , default="فروش کتاب" , editable=False)
    name = models.CharField(max_length=25, blank=True, null=True)
    author = models.CharField(max_length=25, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=3, blank=True, null=True)
    old_price = models.IntegerField(blank=True, null=True)
    new_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=120, blank=True, null=True)

    tag = models.CharField(max_length=50, default="all")

    def __str__(self):
        return self.name
