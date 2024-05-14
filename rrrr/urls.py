from rest_framework.routers import SimpleRouter,DefaultRouter
from .views import CategoryViewSet, create_category, get_categories,delete_category, ProductViewSet
from django.urls import path

# router=SimpleRouter()
router=DefaultRouter()

router.register("categories",CategoryViewSet)
router.register("products",ProductViewSet)

urlpatterns=[
    path("get_categories/",get_categories),
    path("create_category/",create_category),
    path("delete_category/<int:pk>/",delete_category)
]
urlpatterns+=router.urls