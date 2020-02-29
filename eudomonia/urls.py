from django.contrib import admin
from django.urls import path,include
from . import views

 
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('accounts/', include('accounts.urls')),
    
=======
    path('communicable/', views.communicable),
>>>>>>> 5517c7ec4ce7ccd291c84a9a2330fae103817b83
    
]
