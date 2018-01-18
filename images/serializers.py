from rest_framework import serializers

from . import models

class ImageSerializer(serializers.ModelSerializer):
    """Serializes a category for our Image API"""

    class Meta:
        model = models.Image
        fields = ['id', 'url', 'date_created']
    
    def create(self, validated_data):
        """Create and return a new image."""

        image = models.Image(
            url = validated_data['url'],
            uploaded_by = self.context['request'].user
        )

        image.save()

        return image