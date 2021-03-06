from django.contrib.auth.models import User
from .serializers import CategorySerializers, PublicationSerializers, StatusSerializers
# Models
from category.models import Category
from publication.models import Publication
from status.models import Status
# restframework
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

#Root
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'category': reverse('category-list', request=request, format= format),
        'status': reverse('status-list', request=request, format= format),
        'publication': reverse('publication-list', request=request, format=format)
    })

# Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


# Publications

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializers

# Status

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers




