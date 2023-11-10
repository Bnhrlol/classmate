from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Classmate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})
