"""
Serializers for Recipe API
"""
from rest_framework import serializers

from core.models import (
    Recipe,
    Tag,
)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serializer for recipe detail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag view"""

    class Meta(RecipeSerializer.Meta):
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
