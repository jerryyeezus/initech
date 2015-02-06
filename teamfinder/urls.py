__author__ = 'yee'
from django.conf.urls import url
from teamfinder import views

urlpatterns = [
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^register/$', views.UserAccountViewSet.as_view({'post': 'create', 'get': 'list'})),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^prof_logout/$', views.LogoutView.as_view()),
    url(r'^courses/$', views.CourseAdd.as_view()),
    url(r'^courses/(?P<pk>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.CourseList.as_view()),
    url(r'^groups/$', views.GroupViewList.as_view()),
    url(r'^group_add/$', views.GroupAdd.as_view()),
    url(r'^students/(?P<pk>\w+)/$', views.StudentDetail.as_view())
]