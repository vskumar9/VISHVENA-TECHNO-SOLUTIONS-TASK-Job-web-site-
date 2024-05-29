from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobSeekerViewSet, AdminUserViewSet, JobViewSet
from . import views_html as views

router = DefaultRouter()
router.register(r'jobseekers', JobSeekerViewSet)
router.register(r'adminusers', AdminUserViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home', views.home, name='home'),
    path('jobseeker/create/', views.jobseeker_create, name='jobseeker_create'),
    path('jobseeker/update/<uuid:id>/', views.jobseeker_update, name='jobseeker_update'),
    path('jobseeker/delete/<uuid:id>/', views.jobseeker_confirm_delete, name='jobseeker_confirm_delete'),
    path('jobseeker/list/', views.jobseeker_list, name='jobseeker_list'),
    path('adminuser/create/', views.adminuser_create, name='adminuser_create'),
    path('adminuser/update/<uuid:id>/', views.adminuser_update, name='adminuser_update'),
    path('adminuser/delete/<uuid:id>/', views.adminuser_delete, name='adminuser_confirm_delete'),
    path('adminuser/list/', views.adminuser_list, name='adminuser_list'),
    path('job/create/', views.job_create, name='job_create'),
    path('job/update/<uuid:id>/', views.job_update, name='job_update'),
    path('job/delete/<uuid:id>/', views.job_delete, name='job_confirm_delete'),
    path('job/list/', views.job_list, name='job_list'),
]
