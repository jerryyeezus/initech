__author__ = 'yee'
from django.conf.urls import url
from teamfinder import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^register/$', views.UserAccountViewSet.as_view({'post': 'create', 'get': 'list'})),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),

    url(r'^add_courses/$', views.CourseAdd.as_view()),
    url(r'^courses/(?P<prof>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.CourseList.as_view()),

    url(r'^add_assignment/$', views.AddAssignment.as_view()),
    url(r'^assignments/(?P<which_course>\w+)/$', views.AssignmentList.as_view()),

    # url(r'^groups/$', views.GroupViewList.as_view()),
    # url(r'^group_add/$', views.GroupAdd.as_view()),


    url(r'^students/(?P<pk>\w+)/$', views.StudentDetail.as_view()), # TODO remove
    url(r'^add_student/$', views.AddStudent.as_view()), # TODO remove
    url(r'^students/$', views.StudentList.as_view()), # TODO remove
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
