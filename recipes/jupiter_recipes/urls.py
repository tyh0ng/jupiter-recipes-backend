from django.urls import path, include
from . import views

urlpatterns = [
    path('recipes/<str:username>', views.recipe_get, name="recipes-all"),
    path('recipes/', views.recipe_create, name="recipes-create"),
    path('products/<str:keyword>', views.product_get, name="product-get"),
    path('rest-auth/', include('rest_auth.urls'))
]