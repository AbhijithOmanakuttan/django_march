from django.urls import path
from . import views

urlpatterns=[
    path('home',views.abit),
    path('hint',views.alllists),
    path('getlist/<int:id>',views.getlists),
    path('dont',views.alldontu),
    path('getdontu/<int:id>',views.getdontu),
    path('addli',views.adddon),
    path('hello/<int:id>',views.donts)

]