__author__ = 'yee'
from django.conf.urls import url
from teamfinder import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^register/$', views.UserAccountViewSet.as_view({'post': 'create', 'get': 'list', 'put': 'update'})),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^courses/(?P<prof>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.CourseList.as_view()),
    url(r'^student_courses/(?P<student>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.StudentCourseList.as_view()),
    url(r'^assignments/(?P<which_course>\w+)/$', views.AssignmentList.as_view()),
    url(r'^roster/(?P<pk>\d+)/$', views.CourseRoster.as_view()),
    url(r'^teams/(?P<ass_pk>\d+)/$', views.CourseTeams.as_view()),
    url(r'^add_assignment/$', views.AddAssignment.as_view()),
    url(r'^add_courses/$', views.CourseAdd.as_view()),
    url(r'^add_import/$', views.CourseUpload.as_view()),
    url(r'^generate_teams/$', views.GenerateTeams.as_view()),
    url(r'^add_team/$', views.AddTeam.as_view()),
    url(r'^add_thing/$', views.AddThing.as_view()),
    # url(r'^add_thing/$', views.AddThing.as_view()),
    url(r'^questions/$', views.QuestionView.as_view()),
    url(r'^questions/(?P<which_course>\d+)$', views.QuestionView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
