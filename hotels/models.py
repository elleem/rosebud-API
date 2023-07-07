from django.contrib.auth import get_user_model
from django.db import models

class Hotel(models.Model):
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
