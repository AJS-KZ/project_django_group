from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from articles.models import Article, ArticleFile
from articles.serializers import (
    ArticleAllSerializer,
    ArticleFileAllSerializer,
    ArticleListSerializer,
    ArticleCreateSerializer
)


class ArticleFileViewSet(APIView):
    queryset = ArticleFile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ArticleFileAllSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            try:
                object = self.queryset.get(id=pk)
                serializer = self.serializer_class(object).data
                return Response(data=serializer, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                raise Http404
        serializer = self.serializer_class(
            instance=self.queryset.all(),
            many=True
        )
        return Response(data={"detail": 'OK',
                              "data": serializer.data},
                        status=status.HTTP_200_OK)


class ArticleViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleAllSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'list':
            serializer_class = ArticleListSerializer
        elif self.action == 'create':
            serializer_class = ArticleCreateSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={}, status=status.HTTP_201_CREATED)
