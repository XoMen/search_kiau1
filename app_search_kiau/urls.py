from django.urls import path
from app_search_kiau import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('' , views.home , name="Search Kiau"),
path('login/' , views.login_, name="login"),
path('logout/' , views.logout_ , name="logout")




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
