from django.urls import path
from .views import PostListApi




urlpatterns=[

path('api/posts', PostListApi.as_view(),name='post-list-api'),

]

