from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloWorldAPI(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Return a list of APIView Features"""
        an_apiview = [
            'Uses HTTP method as function(get, post, patch, delete, put)',
            'Is similar to traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':"Hello", 'an_apiview': an_apiview})

    def post(self, request):
        """Hello Message with our Name"""
        serializer = self.serializer_class(data=request.data)
        print("request.data is ", request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handles in updating the object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handles in partial updating the object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handles in deleting the object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a Hello Message[Similar to get method]"""

        a_viewset = [
            "Uses Actions(List, create, retrieve, update, partial update)",
            "Automatocally maps the urls using Routers",
            "Provides more functionality with less code"
        ]
        return Response({'message': "Hello", 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object """

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle deleting an object"""

        return Response({'http_method':'DELETE'})
