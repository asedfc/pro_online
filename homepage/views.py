from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, HomePicSerializer

from .models import HomePic

# Create your views here.
def homepage(request):
    return HttpResponse("Hello， World! from homepage.view")

def index(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']


    return render(request, 'watch_index.html')

#class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HomePicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomePic.objects.filter(show=True)
    serializer_class = HomePicSerializer