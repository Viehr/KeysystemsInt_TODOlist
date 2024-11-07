from django.shortcuts import render


# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Author, Post, Tag
from .serializers import AuthorSerializer, PostSerializer, TagSerializer


class AuthorListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=204)


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]