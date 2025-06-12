from django.urls import path
from .views import home, about, coc, resources, login, signup

app_name = "website" 
urlpatterns = [
    path('', home, name ="home"),
    path('about/', about, name ="about"),
    path('coc/', coc, name ="coc"),
    path('resources/', resources, name ="resources"),
    path('login/', login, name ="login"),
    path('signup/', signup, name ="signup"),
]
