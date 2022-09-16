
from django.db import models
class registermod(models.Model):
    userid=models.EmailField(primary_key=True)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.userid +","+ self.password
