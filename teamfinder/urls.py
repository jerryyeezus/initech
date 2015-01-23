__author__ = 'yee'
from django.conf.urls import url
from teamfinder import views

urlpatterns = [
    url(r'^students/$', views.StudentList.as_view()),
    # url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view())
    url(r'^students/(?P<pk>\w+)/$', views.StudentDetail.as_view())
]