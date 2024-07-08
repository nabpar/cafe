from rest_framework import serializers
from .models import Category,Product,Table,Order,Bill
from rest_framework import filters


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Category_SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Product_SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','table','category','product','description','quantity','total_price','ordered_date')

 
class BillSearilizer(serializers.ModelSerializer):
        model = Bill
        fields = '__all__'