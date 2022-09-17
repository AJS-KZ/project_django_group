from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from products.models import Book
from products.serializers import BookAllSerializer, BookListSerializer, BookCreateSerializer


class BookViewSet(APIView):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookAllSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            serializer = self.serializer_class(self.queryset.all(), many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            try:
                instance = self.queryset.get(id=pk)
                serializer = self.serializer_class(instance)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(data={'ERROR': 'by given pk object not found!'},
                                status=status.HTTP_400_BAD_REQUEST)

    def post(self, requset, *args, **kwargs):
        serializer = BookCreateSerializer(data=requset.data)
        serializer.is_valid(raise_exception=True)  # --> Проверка на валидность
        instance = serializer.save()
        s = BookListSerializer(instance)
        return Response(data=s.data, status=status.HTTP_201_CREATED)
