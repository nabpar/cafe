from django.db import models
from django.core.exceptions import ValidationError
import os
# Create your models here.
def image_validate(value):
    allowed_extensions = [".png",".jpeg",".jpg"]
    file_extensions = value.name.split('.')[-1].lower()
    if '.'+ file_extensions not in allowed_extensions:
        raise ValidationError(f"only {allowed_extensions} are allowed")

def image_upload_path(self,filename):
    return os.path.join('media',filename)



#  CLASS FOR CATEGORY
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_img = models.ImageField(upload_to= image_upload_path,validators= [image_validate],blank=True,null=True)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category = models.ForeignKey(Category , on_delete= models.CASCADE )
    product_name = models.CharField(max_length=255)
    product_price = models.PositiveIntegerField()
    product_img = models.ImageField(upload_to=image_upload_path,validators=[image_validate],blank=True,null=True)

    def __str__(self):
        return self.product_name

class Table(models.Model):
    table_name = models.CharField(max_length=255,default = "TABLE_NO:")
    table_img = models.ImageField(upload_to=image_upload_path,validators=[image_validate],blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table_name

class Order(models.Model):
    table = models.ForeignKey(Table,on_delete=models.CASCADE, default="CHOOSE THE TABLE NO:")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True) 


    def save(self,*args,**kwargs):
        self.total_price = self.calculate_total_price()
        super().save(*args,**kwargs)

    def calculate_total_price(self):
        # product =self.product.product_price
        price = self.product.product_price * self.quantity
        return price

    
    def __str__(self):
        return self.product.product_name
    

class Bill(models.Model):
    table_no = models.ForeignKey(Table,on_delete=models.CASCADE,blank=True,null=True)
    order_items= models.ManyToManyField(Order)
    total_amount = models.PositiveIntegerField(blank=True, null=True)
    paid_amount = models.PositiveIntegerField(blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid')  
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new instance
            super().save(*args, **kwargs)  # Save the Bill first to get an id
        self.table_no = self.order_items.first().table  # Assuming you want the first order's table
        self.total_amount = sum(order.total_price for order in self.order_items.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"(Table No: {self.table_no})"

    def mark_as_paid(self):
        self.paid_amount = self.total_amount
        self.payment_status = 'Paid'
        self.save()