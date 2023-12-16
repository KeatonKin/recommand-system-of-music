from django.db import models


class Test(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return super().__str__()
    