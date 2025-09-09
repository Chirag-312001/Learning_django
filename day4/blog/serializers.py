from rest_framework import serializers
from .models import Posts

class PostSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name',read_only=True)

    class Meta:
        model=Posts
        fields = ['id','title', 'content','created_at','author_name']
