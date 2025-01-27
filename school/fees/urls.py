# urls.py
from django.contrib import admin
from django.urls import path
from fees.views import ans, ans2,ans3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ans3),
    path('app133213424/', ans, name='home'), 
    path('app24234324/', ans2, name='fees'), 
]
