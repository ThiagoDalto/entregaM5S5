from rest_framework.views import APIView, status, Response
from rest_framework.generics import ListCreateAPIView
from .models import Album
from users.models import User
from users.serializers import UserSerializer 
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class AlbumView(APIView, PageNumberPagination):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request):
#         """
#         Obtençao de albums
#         """
#         albums = Album.objects.all()

#         result_page = self.paginate_queryset(albums, request)
#         serializer = AlbumSerializer(result_page, many=True)

#         return self.get_paginated_response(serializer.data)

#     def post(self, request):
#         """
#         Criaçao de album
#         """
#         serializer = AlbumSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=request.user)

#         return Response(serializer.data, status.HTTP_201_CREATED)


class AlbumView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)
