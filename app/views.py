from django.shortcuts import render
from app.models import User
from app.Serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.
# views.py

from rest_framework import viewsets

class usrList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST', 'DELETE'])
def add_user(request):
    
 
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = UserSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)