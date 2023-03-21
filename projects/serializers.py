from rest_framework import serializers
from projects.models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    """
        Project Image serializer class
    """
    class Meta:
        model = ProjectImage
        fields = ['media', 'project']
        lookup_field = 'uuid'


class ProjectSerializer(serializers.ModelSerializer):
    """
        Project serializer class
    """
    images = ProjectImageSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields=['title', 'description', 'short_desc', 'link', 'thumbnail', 'slug', 'images', 'created_at']
        lookup_field = 'slug'