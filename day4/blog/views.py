from django.shortcuts import render
from .models import Posts
from .serializers import PostSerializers
from rest_framework.views import APIView
# Create your views here.

from rest_framework.response import Response


class PostListApi(APIView):
    def get(self, request):
        posts = Posts.objects.all().order_by('-created_at')
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)