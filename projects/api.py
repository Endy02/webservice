from rest_framework import status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from projects.models import Project, ProjectImage
from projects.serializers import ProjectSerializer, ProjectImageSerializer


# ----------------------------- Project CRUD Endpoints -----------------------------
class ProjectListApi(ListAPIView):
    """
        Get Project list endpoint
        Role: Allow Any
    """
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateApi(CreateAPIView):
    """
        CREATE new project endpoint
        Role: Is Admin user
    """
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            if request.data.get('images'):
                for image in request.FILES.getlist('images'):
                    medias = {'media' : image, 'project': project.id}
                    image = ProjectImageSerializer(data=medias)
                    if image.is_valid():
                        image.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR , data=serializer.error_messages)



class ProjectApi(RetrieveAPIView):
    """
        RETRIEVE a project endpoint
        Role: Allow Any
    """
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ProjectUpdateAPI(UpdateAPIView):
    """
        UPDATE Project endpoint
        Role: Is Admin user
    """
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ProjectDeleteAPI(DestroyAPIView):
    """
        DELETE Project endpoint
        Role: Is Admin
    """
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
# ----------------------------- END Project Endpoints -----------------------------

# ----------------------------- Project Image Endpoints -----------------------------
class ProjectImageListApi(ListAPIView):
    """
        Get Project list image endpoint
        Role: Allow Any User
    """
    permission_classes = [AllowAny]
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer



class ProjectImageCreateApi(CreateAPIView):
    """
        CREATE new project image endpoint
        Role: Is Admin User
    """
    permission_classes = [AllowAny]
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer

    def post(self, request, format=None):
        serializer = ProjectImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(data={"error": serializer.error_messages, "serializer": request.data} ,status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)



class ProjectImageApi(RetrieveAPIView):
    """
        RETRIEVE a project image endpoint
        Role: Allow Any User
    """
    permission_classes = [AllowAny]
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    lookup_field = 'uuid'


class ProjectImageUpdateAPI(UpdateAPIView):
    """
        UPDATE Project image endpoint
        Role: Is Admin User
    """
    permission_classes = [AllowAny]
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    lookup_field = 'uuid'


class ProjectImageDeleteAPI(DestroyAPIView):
    """
        DELETE Project image endpoint
        Role: Is Admin User
    """
    permission_classes = [AllowAny]
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    lookup_field = 'uuid'
# ----------------------------- END Project Image Endpoints -----------------------------
