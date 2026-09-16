from django.db import models

# Create your models here.
class VerbalAutopsy(models.Model):
    deceased_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    age_at_death = models.IntegerField()
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length=2, choices=[("HO", "Home"), ("HP", "Hospital"), ("O", "Other")])
    respondent_name = models.CharField(max_length=100)
    respondent_relationship = models.CharField(max_length=100)
    interview_date = models.DateField()
    symptoms = models.TextField()
    probable_cause_of_death = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)