from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for for testing APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        print("validated_data is", validated_data)
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            print("password is", password, validated_data)
            instance.set_password(password)

        print("Updating Object")
        return super().update(instance, validated_data)
