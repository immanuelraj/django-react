from copy import deepcopy
from django.db import transaction
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, CategoryListSerializer, \
    ProductListSerializer
from .paginations import PaginateBy20
from rest_framework import generics, filters, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('first_name')
    ordering_fields = '__all__'
    ordering = ('-id',)
    model = Category
    pagination_class = PaginateBy20
    queryset = Category.objects.all()
    lookup_field = 'ext_id'

    def list(self, request):
        import pdb; pdb.set_trace()
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CategoryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CategoryListSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    serializer_class = ProductSerializer
    search_fields = ('name')
    ordering_fields = '__all__'
    ordering = ('-id',)
    model = Product
    pagination_class = PaginateBy20
    queryset = Product.objects.all()
    lookup_field = 'ext_id'

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, ext_id):
        try:
            product = Product.objects.get(ext_id=ext_id)  
            data = ProductListSerializer(product).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "response": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            import pdb; pdb.set_trace()
            req_data = self.request.data
            serializer = self.serializer_class(data=req_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'error', 'response': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "response": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, ext_id):
        try:
            req_data = self.request.data
            product = Product.objects.get(ext_id=ext_id)
            old_data = deepcopy(self.serializer_class(product).data)
            serializer = self.serializer_class(product, data=req_data, partial=True, context={'request': request, 'old_data': old_data})
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        serializer.save(force_update=True)
                except Exception as e:
                    return Response({"status": "error", "response": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                return Response({'status': 'ok'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "response": str(e)}, status=status.HTTP_400_BAD_REQUEST)