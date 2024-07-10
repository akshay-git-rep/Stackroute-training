from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import permissions, serializers
from profiles_api import models
from profiles_api.models import Book, Emp
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request):
        """Returns a list of APIView features"""
        

        return Response({'message': 'Hello!'})
    
    serializer_class = serializers.HelloSerializer

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        # name = request.data.get('name')
        # return Response({'message': f'Hello {name}'}) 

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
class BookApiView(APIView):

    serializer_class = serializers.BookModelSerializer

    def get(self, request):
        """Returns a list of APIView features"""

        books = Book.objects.all().values()
        return Response({'books': list(books)})

    def post(self, request):         
        """post method to add new Book"""         
        serializer = self.serializer_class(data=request.data)         
        if serializer.is_valid():             
            title = serializer.validated_data.get('title')             
            author = serializer.validated_data.get('author')             
            book = Book.objects.create(title=title, author=author)             
            Book.save(book)             
            message = f'Book Added {book}'             
            return Response({'message': message})         
        else:             
            return Response(                 
                serializer.errors,                 
                status=status.HTTP_400_BAD_REQUEST)
        
class BookViewSet(viewsets.ModelViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.BookModelSerializer

    queryset = Book.objects.all()


class EmpApiView(APIView):   

    serializer_class = serializers.EmpModelSerializer 

    def get(self, request):         
        """Returns a list of APIView features""" 

        emps = Emp.objects.all().values()         
        return Response({'emps': list(emps)})
    
    def post(self, request):
        """post method to add new emp"""
 
        serializer = self.serializer_class(data=request.data)
 
        if serializer.is_valid():
            # id = serializer.validated_data.get('id')
            name = serializer.validated_data.get('name')
            salary = serializer.validated_data.get('salary')
            project = serializer.validated_data.get('project')
            emp = Emp.objects.create(name =name, salary=salary, project=project)
            Book.save(emp)
            message = f'Emp Added {emp}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        
class EmpViewSet(viewsets.ModelViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.EmpModelSerializer
 
    queryset =Emp.objects.all() 


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
        # IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
    
