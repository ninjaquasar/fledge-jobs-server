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
    ENTRY_LEVEL = 'ENTRY-LEVEL'
    JUNIOR = 'JUNIOR'
    INTERMEDIATE = 'INTERMEDIATE'
    EXPERT = 'EXPERT'
    FIXED = 'FIXED'
    CONTRACTUAL = 'CONTRACTUAL'
    HOURLY = 'HOURLY'
    PROJECT_BASED = 'PROJECT-BASED'
    LOCATION_TYPE_CHOICES = (
        (ONSITE, "On-Site"),
        (REMOTE, "Remote"),
        (HYBRID, "Hybrid"),
    )
    EXPERTISE_LEVEL_CHOICES = (
        (ENTRY_LEVEL, "Entry-Level"),
        (JUNIOR, "Junior"),
        (INTERMEDIATE, "Intermediate"),
        (EXPERT, "Expert"),
    )
    PRICING_TYPE_CHOICES = (
        (FIXED, "Fixed"),
        (CONTRACTUAL, "Contractual"),
        (HOURLY, "Hourly"),
        (PROJECT_BASED, "Project-based"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    company_name = models.CharField(max_length=75)
    expertise_level = models.CharField(max_length=12, choices=EXPERTISE_LEVEL_CHOICES)
    pricing_type = models.CharField(max_length=13, choices=PRICING_TYPE_CHOICES)
    requirements = models.CharField(max_length=150)
    location = models.CharField(max_length=75)
    location_type = models.CharField(max_length=7, choices=LOCATION_TYPE_CHOICES)
    date_posted = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, related_name='jobs', blank=True, null=True)
    def __str__(self):
        return self.title