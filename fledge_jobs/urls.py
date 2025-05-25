from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="FledgeJobs - API Guide",
        default_version='v1',
        description="API documentation for the FledgeJobs job board web application. It provides information about our RESTful API endpoints and enables developers to interact with and integrate the platform effectively.",
        terms_of_service="https://example.com/policies/terms-of-service/",
        contact=openapi.Contact(email="contact@fledgejobs.jobs"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/', include('api.urls'), name='api'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]