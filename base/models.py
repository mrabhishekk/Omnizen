from django.db import models

# Model is the database schema visible in admin panel.

class Task(models.Model):       # here Task is a database table
    PRIORITY_CHOICES = [
        ('high', '🔴 High Priority'),
        ('medium', '🟡 Medium Priority'),
        ('low', '⚪ Low Priority'),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    completed =  models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    due_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["completed"]

        






# migrations = modificatons/apply modifications
# makemigrations 
# migrate
# register model

