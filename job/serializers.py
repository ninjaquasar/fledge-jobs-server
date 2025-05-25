from rest_framework import serializers
from job.models import Job, Category


class JobSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'description', 'requirements', 'location', 'location_type', 'expertise_level', 'pricing_type', 'category', 'date_posted']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']