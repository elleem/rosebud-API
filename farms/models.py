from django.contrib.auth import get_user_model
from django.db import models

class Farm(models.Model):
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
