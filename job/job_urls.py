from django.urls import path
from job.views import ViewAllJobs, ViewSpecificJob

urlpatterns = [
    path('', ViewAllJobs.as_view(), name='view-jobs'),
    path('<int:id>/', ViewSpecificJob.as_view(), name='view-specific-job'),
]
