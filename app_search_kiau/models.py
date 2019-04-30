from django.db import models


class post(models.Model):
    # image = models.ImageField(upload_to=post_pictures/)
    title = models.CharField(max_length=120, blank=True, null=True)

    description = models.TextField(max_length=120, blank=True, null=True)

    tag = models.CharField(max_length=50, default="all")

    def __str__(self):
        return self.title
