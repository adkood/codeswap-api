from django.db import models

# Create your models here.


class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.TextField()
    language = models.CharField(max_length=50, choices=[
        ('python', 'Python'),
        ('java', 'Java'),
        ('javascript', 'JavaScript'),
        ('c', 'C'),
        ('cpp', 'C++'),
        ('php', 'PHP'),
        ('ruby', 'Ruby'),
    ], default='cpp')

    def __str__(self):
        return f'Room {self.id,self.language}'
