from django.db import models
from datetime import date

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    STATUS_CHOICES = [
        ('ENP', 'En Proceso'),
        ('FIN', 'Finalizado'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='ENP')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    STATUS_CHOICES = [
        ('PEN', 'Pendiente'),
        ('REA', 'Realizada'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    date = models.DateField()

    def __str__(self) -> str:
        return self.title