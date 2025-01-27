from django.contrib import admin
from django.urls import path
from course.views import ans
urlpatterns = [
    path('admin/', admin.site.urls),
   path('app1/',ans)
]
