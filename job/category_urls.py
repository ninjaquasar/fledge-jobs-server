from django.urls import path
from job.views import ViewAllCategories, ViewSpecificCategory

urlpatterns = [
    path('', ViewAllCategories.as_view(), name='view-categories'),
    path('<int:id>/', ViewSpecificCategory.as_view(), name='view-specific-category'),
]