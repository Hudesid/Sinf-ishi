from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = (
        ('cp', 'Completed'),
        ('ip', 'In Progress'),
        ('fl', 'Failed'),
    )

    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.due_date < timezone.now() and self.status != 'cp':
            self.status = 'fl'
        return super().save(*args, **kwargs)

