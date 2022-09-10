from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from articles.models import Article, ArticleFile
from articles.serializers import (
    ArticleAllSerializer,
    ArticleFileAllSerializer,
    ArticleListSerializer,
    ArticleCreateSerializer
)


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
