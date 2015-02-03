__author__ = 'yee'
from django.conf.urls import url
from teamfinder import views

urlpatterns = [
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^prof_register/$', views.ProfessorAccountViewSet.as_view({'post': 'create', 'get': 'list'})),
    url(r'^prof_login/$', views.ProfessorLoginView.as_view()),
    url(r'^groups/$', views.GroupViewList.as_view()),
    url(r'^group_add/$', views.GroupAdd.as_view()),
    # url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view())
    url(r'^students/(?P<pk>\w+)/$', views.StudentDetail.as_view())
]