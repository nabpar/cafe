from django.contrib import admin
from .models import Category,Product,Table,Order,Bill

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','category_img']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','category','product_name','product_price','product_img']
admin.site.register(Product,ProductAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display = ['id','table_name','table_img','date_created']
admin.site.register(Table,TableAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','table','category','product','description','quantity','total_price','ordered_date']
admin.site.register(Order,OrderAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = ('table_no','total_amount','paid_amount', 'payment_status', 'created_at','get_order_items')
    # search_fields = ('table_no',)
    # readonly_fields = ('total_amount', 'created_at', )
    # list_filter = ('payment_status',)

    def get_order_items(self, obj):
        return ", ".join([order.product.product_name for order in obj.order_items.all()])
    get_order_items.short_description = 'Order Items'

    
    def save_model(self, request, obj, form, change):
        obj.total_amount = obj.order_items.total_price
        super().save_model(request, obj, form, change)

admin.site.register(Bill, BillAdmin)

