from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK as OK, HTTP_201_CREATED as CREATED, HTTP_204_NO_CONTENT as NO_CONTENT, HTTP_400_BAD_REQUEST as BAD_REQUEST, HTTP_404_NOT_FOUND as NOT_FOUND
from job.models import Job, Category
from job.serializers import JobSerializer, CategorySerializer


class ViewAllJobs(APIView):
    """
    #### API Endpoint for managing Job lists
    - Allows admins to create job posts
    - Allows authenticated users to browse, and filter jobs
    """
    def get(self, request):
        jobs = Job.objects.all()
        response = JobSerializer(jobs, many=True)
        return Response({
            "message": "Successfully fetched all job posts",
            "data": response.data,
        }, OK)
    def post(self, request):
        """ #### Create a new job post (Access: Admin) """
        response = JobSerializer(data=request.data)
        if response.is_valid():
            response.save()
            return Response({
                "message": "Successfully created a job post",
                "data": response.data,
            }, CREATED)
        else:
            return Response(response.errors, BAD_REQUEST)

class ViewSpecificJob(APIView):
    """
    #### API Endpoint for managing a specific Job
    - Allows admins to update and delete a job post
    - Allows authenticated users to view and apply on a job
    """
    def get(self, request, id):
        try:
            job = Job.objects.get(pk=id)
            response = JobSerializer(job)
            return Response({
                "message": f"Successfully fetched the specified job post",
                "data": response.data,
            }, OK)
        except Job.DoesNotExist:
            return Response({
                "message": f"Failed to fetch the specified job post"
            }, NOT_FOUND)
    def put(self, request, id):
        """ #### Update the job post (Access: Admin) """
        job = Job.objects.get(pk=id)
        response = JobSerializer(job, data=request.data)
        if response.is_valid():
            response.save()
            return Response({
                "message": f"The job post is successfully updated",
                "data": response.data
            }, OK)
        else:
            return Response({
                "message": "Provided data is invalid",
            }, BAD_REQUEST)
    def delete(self, request, id):
        """ #### Delete the job post (Access: Admin) """
        job = Job.objects.get(pk=id)
        job_copy = job
        job.delete()
        response = JobSerializer(job_copy)
        return Response({
            "message": "The job post is successfully deleted",
            "data": response.data,
        }, NO_CONTENT)

class ViewAllCategories(APIView):
    """
    #### API Endpoint for managing Categories
    - Allows admins to create categories
    - Allows authenticated users to browse categories
    """
    def get(self, request):
        categories = Category.objects.all()
        response = CategorySerializer(categories, many=True)
        return Response({
            "message": "Successfully fetched all categories",
            "data": response.data,
        }, OK)
    def post(self, request):
        """ #### Create a category (Access: Admin) """
        response = CategorySerializer(data=request.data)
        if response.is_valid():
            response.save()
            return Response({
                "message": "Successfully created a category",
                "data": response.data,
            }, CREATED)
        else:
            return Response(response.errors, BAD_REQUEST)

class ViewSpecificCategory(APIView):
    """
    #### API Endpoint for managing a specific Category
    - Allows admins to update and delete a category
    - Allows authenticated users to view a category
    """
    def get(self, request, id):
        try:
            category = Category.objects.get(pk=id)
            response = CategorySerializer(category)
            return Response({
                "message": f"Successfully fetched the specified category",
                "data": response.data,
            }, OK)
        except Category.DoesNotExist:
            return Response({
                "message": f"Failed to fetch the specified category because it does not exists."
            }, NOT_FOUND)
    def put(self, request, id):
        """ #### Update the category (Access: Admin) """
        category = Category.objects.get(pk=id)
        response = CategorySerializer(category, data=request.data)
        if response.is_valid():
            response.save()
            return Response({
                "message": f"Category no.{id} is successfully updated",
                "data": response.data
            }, OK)
        else:
            return Response({
                "message": "Provided data is invalid",
            }, BAD_REQUEST)
    def delete(self, request, id):
        """ #### Delete the category (Access: Admin) """
        category = Category.objects.get(pk=id)
        category_copy = category
        category.delete()
        response = CategorySerializer(category_copy)
        return Response({
            "message": "The category is successfully deleted"
        }, NO_CONTENT)
