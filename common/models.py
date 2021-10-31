from datetime import datetime
from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'Departments'

class Quote(models.Model):
    tag = models.ForeignKey('Departments', on_delete=models.CASCADE, default=1)
    content = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.tag}: {self.content} : {self.date_created}'

    # class Meta:
    #     verbose_name_plural = 'Quote'