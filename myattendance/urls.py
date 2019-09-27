from django.urls import path
from . import views

urlpatterns = [
   path('dashboard/',views.dashboard, name='dashboard'), 
   path('dashboard/update/<int:p>',views.updateinfo, name='update'),
   path('dashboard/edit/<int:sb>',views.editinfo, name='edit'),
   #path(r'dashboard/edit/(?P<pk>\d+)/$',views.editinfo, name='edit'),
   path('dashboard/update/addsubject/', views.addsubject, name='addsubject'),
   path('dashboard/addsubject/addsubject', views.addsubject, name='addsubject'),
   path('dashboard/addsubject/', views.addsubject, name='addsubject'),
   path('dashboard/delete/addsubject/', views.addsubject, name='addsubject'),
   path('dashboard/addsubject/updatesubjectinfo', views.addsubjecttodatabase, name='addsubjecttodatabase'),
   path('dashboard/delete/addsubject/updatesubjectinfo', views.addsubjecttodatabase, name='addsubjecttodatabase'),
   path('dashboard/delete/<int:sb>',views.deletesubject, name='delete'),
]