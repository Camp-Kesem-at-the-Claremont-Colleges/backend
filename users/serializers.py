from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ['username', 'role', 'first_name', 'last_name', 
        'bio', 'avatar', 'is_staff',
        'camp_name', 'password']
        read_only_fields = ['is_staff']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'username': {
                'write_only': True
            }
        }

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.camp_name = validated_data.get('camp_name', instance.camp_name)
        instance.role = validated_data.get('role', instance.role)
        if validated_data.get('password', None):
            instance.set_password(validated_data['password'])

        instance.save()

        return instance

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            username=validated_data['username'],
            camp_name=validated_data['camp_name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role']
        )

        if (user.role == 'Director' or user.role == 'Program Director'):
            user.is_staff = True

        user.set_password(validated_data['password'])

        user.save()

        return user
