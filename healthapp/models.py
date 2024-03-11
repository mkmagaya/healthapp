from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # fixing admin plurals
    class Meta:
        verbose_name_plural = 'Data'

    # defining table object name
    def __str__(self):
        return self.name