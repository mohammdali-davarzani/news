from rest_framework import serializers

from .models import NewsContents


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContents
        fields = "__all__"
