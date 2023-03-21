from django.urls import path
from projects import api


urlpatterns = [
    path('', api.ProjectListApi.as_view(), name='api-projects'),
    path('<slug:slug>', api.ProjectApi.as_view(), name='api-single-project'),
    path('create/', api.ProjectCreateApi.as_view(), name='api-create-project'),
    path('<slug:slug>/delete', api.ProjectDeleteAPI.as_view(), name='api-delete-project'),
    path('<slug>/update', api.ProjectUpdateAPI.as_view(), name='api-update-project'),
    
    path('project-images/<uuid>', api.ProjectImageApi.as_view(), name='api-single-project-image'),
    path('project-images/create/', api.ProjectImageCreateApi.as_view(), name='api-create-project-image'),
    path('project-images/<uuid>/update', api.ProjectImageUpdateAPI.as_view(), name='api-update-project-image'),
    path('project-images/<uuid>/delete', api.ProjectImageDeleteAPI.as_view(), name='api-delete-project-image'),
    path('project-images/<uuid>/delete', api.ProjectImageDeleteAPI.as_view(), name='api-delete-project-image'),
]