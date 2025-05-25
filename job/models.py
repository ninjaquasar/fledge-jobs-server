from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Job(models.Model):
    ONSITE = 'ON-SITE'
    REMOTE = 'REMOTE'
    HYBRID = 'HYBRID'
    LOCATION_TYPE_CHOICES = (
        (ONSITE, "On-Site"),
        (REMOTE, "Remote"),
        (HYBRID, "Hybrid"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    company_name = models.CharField(max_length=75)
    requirements = models.CharField(max_length=150)
    location = models.CharField(max_length=75)
    location_type = models.CharField(max_length=7, choices=LOCATION_TYPE_CHOICES)
    date_posted = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, related_name='jobs', blank=True, null=True)
    def __str__(self):
        return self.title