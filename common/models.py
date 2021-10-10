from datetime import datetime
from django.db import models

class Quote(models.Model):
    content = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.content} : {self.date_created}'

    # class Meta:
    #     verbose_name_plural = 'Quote'