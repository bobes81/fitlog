from django.db import models

class WorkoutEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    workout_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    intensity = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ]
    )
    bmi = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.workout_type} ({self.intensity})"

# Added Workout model
class Workout(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


