from django.contrib.admin import site
from job.models import Category, Job


site.register(Job)
site.register(Category)