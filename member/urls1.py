from django.urls import path
from member.views import *


app_name = 'member'
urlpatterns = [
    path('', MemListView.as_view() , name='list'),
    path('add/', MemAddView.as_view() , name='add'),
    path('detail/<int:pk>', MemDetailView.as_view() , name='detail'),
    path('edit/<int:pk>', MemUpView.as_view() , name='update'),
    path('remove/<int:pk>', MemReView.as_view() , name='remove'),
    path('login/', login, name='login'),
    path('login_ok/', login_ok, name='login_ok'),
]
