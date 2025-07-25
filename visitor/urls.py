
from django.contrib import admin

from django.urls import path

from . import views


urlpatterns = [
   path('add/',views.visitor_from_view,name='add-form'),
   path('sum/',views.visitors_list,name='list'),
   path('edit/<int:id>',views.visitor_edit_list,name='edit'),
   path('delete/<int:id>',views.visitor_delete_list,name='delete'),

]
