from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorListCreateAPIView, AuthorDetailAPIView, TagListCreateView, TagDetailView, PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('', include(router.urls)),
]