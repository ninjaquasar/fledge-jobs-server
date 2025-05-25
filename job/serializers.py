from rest_framework import serializers
from job.models import Job, Category


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'description', 'requirements', 'location', 'location_type', 'date_posted', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']