from django.urls import path
from . import views

app_name = 'online_enrollment'  # This is important for namespaced URLs

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('students/', views.student_list, name='students'),
     path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    path('courses/', views.course_list, name='courses'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/edit/<int:id>/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),
    
     path('enrollment/', views.enrollment_list, name='enrollment_list'),
    path('enrollment/add/', views.enrollment_add, name='enrollment_add'),
    path('enrollment/<int:id>/edit/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollment/<int:id>/delete/', views.enrollment_delete, name='enrollment_delete'),

]
