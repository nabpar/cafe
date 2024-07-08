from django.shortcuts import render
from rest_framework import generics
from .models import Category,Product,Table,Order,Bill
from .serializer import (CategorySerializer,Category_SearchSerializer,
                         ProductSerializer,Product_SearchSerializer,
                         TableSerializer,
                         OrderSerializer,
                         BillSearilizer)
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CategoryFilter
# Create your views here.


#  VIEWS FOR CATEGORY
class CategorySearch(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_SearchSerializer
    filter_backends = [DjangoFilterBackend]
    filerset_class = CategoryFilter

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# VIEWS FOT THE PRODUCT

class ProductSearch(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_SearchSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['^product_name','product_name']

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#  VIEWS FOT THE TABLE

class TableView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


#  VIEWS FOT THE ORDER

class OrderByCategoryView(generics.ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        
        return Product.objects.filter(category_id = category_id)

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


#  VIEWS FOT HE BILL

class BillView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSearilizer

class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSearilizer