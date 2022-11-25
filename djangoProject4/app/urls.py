from django.urls import path, include
from .views import SchoolViewSet
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'school', SchoolViewSet, basename='school')


urlpatterns = [
    path(r'app/', include(router.urls)),
    path(r'tmp_school_list/', views.SchoolList.as_view(), name='tmp_school-list'),
    path(r'tmp_school_create/', views.SchoolCreate.as_view(), name='tmp_school-create'),
    path(r'tmp_school_detail/<str:name>/', views.SchoolDetail.as_view(), name='tmp_school-detail'),
    path(r'tmp_school-list/<str:name>/tmp_school_delete/', views.SchoolDelete.as_view(),
         name='tmp_school-delete'),
    path(r'tmp_school-list/<str:name>/school_class-list/', views.SchoolClassList.as_view(), name='school_class-list'),
    path(r'tmp_school-list/<str:name>/school_class_create/', views.SchoolClassCreate.as_view(), name='school_class-create'),
    path(r'school_class-detail/<int:pk>/', views.SchoolClassDetail.as_view(), name='school_class-detail'),
    path(r'tmp_school_list/<str:name>/school_class-list/<str:className>/school_class_delete/', views.SchoolClassDelete.as_view(),
         name='school_class-delete'),
    path(r'tmp_school_list/<str:name>/school_class_list/<str:className>/student_list/', views.StudentList.as_view(), name='student-list'),
    path(r'student_detail/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path(r'tmp_school_list/<str:name>/school_class-list/<str:className>/student_list/<str:studentName>/student_delete/',
         views.StudentDelete.as_view(),
         name='student-delete'),
]