from django.db import models
from accounts.models import Student

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}"