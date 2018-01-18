from rest_framework import serializers
from django.utils.text import slugify

from . import models

from images.models import Image
from images.serializers import ImageSerializer

from users.serializers import UserProfileSerializer

class TagSerializer(serializers.Serializer):
    """Serializes a tag for our Tag API"""
    label = serializers.CharField()

    class Meta:
        model = models.Tags
        fields = ['id', 'label']
    
    def create(self, validated_data):
        tag = models.Tags(
            label=validated_data['label'],
        )
        tag.save()

        return tag

class ArticleSerializer(serializers.ModelSerializer):
    """Serializes a name field for our Article API"""

    author = UserProfileSerializer(read_only=True)
    cover_photo = ImageSerializer(read_only=True)
    image = serializers.IntegerField(write_only=True)
    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'slug', 'blurb',
        'author', 'cover_photo', 
        'is_published', 'tags',
        'views', 'content', 
        'date_created', 'date_updated', 'image']
        read_only_fields = ['id', 'slug', 'author', 'views']

    def update(self, instance, validated_data):
        tags = validated_data.get('tags', None)
        if tags:
            instance.tags.clear()
            for tag in tags:
                tag_qs = models.Tags.objects.filter(label__iexact=tag['label'])
                if tag_qs.exists():
                    tag = tag_qs.first()
                else:
                    tag = models.Tags.objects.create(**tag)
                instance.tags.add(tag)

        image = validated_data.get('image', None)
        if image:
            image = Image.objects.get(id=image)
            instance.cover_photo = image
        instance.title = validated_data.get('title', instance.title)
        instance.slug = slugify(instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.blurb = validated_data.get('blurb', instance.blurb)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.updated_by = self.context['request'].user

        instance.save()

        return instance

    def create(self, validated_data):
        """Create a new Article"""
        image = Image.objects.get(id=validated_data['image'])
        article = models.Article(
            title = validated_data['title'],
            slug = slugify(validated_data['title']),
            blurb = validated_data['blurb'],
            author = self.context['request'].user,
            updated_by = self.context['request'].user,
            cover_photo = image,
            content = validated_data['content']
        )
        article.save()
        tags = validated_data.get('tags', [])
        for tag in tags:
            tag_qs = models.Tags.objects.filter(label__iexact=tag['label'])
            if tag_qs.exists():
                tag = tag_qs.first()
            else:
                tag = models.Tags.objects.create(**tag)
            article.tags.add(tag)

        return article