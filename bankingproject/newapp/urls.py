from.import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('add/logout',views.logout,name='logout'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches')  # AJAX
]

