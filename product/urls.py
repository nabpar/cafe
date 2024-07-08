

from django.urls import path
from.import views

urlpatterns = [
    #  For Category
    path("category/",views.CategoryView.as_view(),name= "create and shows list of category"),
    path('categorydetail/<int:pk>/',views.CategoryDetail.as_view(),name="retrive,update,delete category"),
    path("categorysearch/",views.CategorySearch.as_view(),name = "search the category"),

    # For Product
    path("product/",views.ProductView.as_view(),name = "list and create product"),
    path('productdetail/<int:pk>/',views.ProductDetail.as_view(),name="retrive,update,delete product"),
    path('productsearch/',views.ProductSearch.as_view(),name="search the product"),

    #  for table
    path("table/",views.TableView.as_view(),name = "list and create table"),
    path('tabledetail/<int:pk>/',views.TableDetail.as_view(),name="retrive,update,delete table"),
    

    #  for order
    path("order/",views.OrderView.as_view(),name = "list and create order"),
    path("orderlisted_bycategory/<int:category_id>/",views.OrderByCategoryView.as_view(),name = "list order by category"),
    path('orderdetail/<int:pk>/',views.OrderDetail.as_view(),name="retrive,update,delete order"),
    # path('productsearch/',views.ProductSearch.as_view(),name="search the product"),

    # for bill
    path("bill/",views.BillView.as_view(),name="list and create bill"),
    path("billdetail/<int:pk>/",views.BillDetail.as_view(),name = ("retrive,update,delete bill")),

]