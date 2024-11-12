from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("user_app.urls")),
    path("chat/" , include("chat_app.urls"))
]