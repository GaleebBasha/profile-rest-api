from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
