from django.urls import path
from .views import home,Registration,update,deletepage



urlpatterns = [
    path('',home,name='home'),
    path('Registration',Registration,name='Registration'),
    path('update/<id>',update,name='update'),
    path('delete/<id>',deletepage,name='deletepage'),
]