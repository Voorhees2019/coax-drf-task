from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.products.api.v1.routes")),
    path("api/v1/", include("apps.orders.api.v1.routes")),
]
