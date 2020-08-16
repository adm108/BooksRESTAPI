from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.api import views as qv

router = DefaultRouter()
router.register(r"books", qv.BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
