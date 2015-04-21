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
    url(r'^add_request/$', views.RequestAdd.as_view()),
    url(r'^requests/(?P<which_team>\d+)/$', views.RequestView.as_view()),
    url(r'^add_thing/$', views.AddThing.as_view()),
    url(r'^notifications/$', views.AddNotification.as_view()),
    url(r'^notifications/(?P<to>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.AddNotification.as_view()),
    url(r'^add_lfg/$', views.AddLFG.as_view()),
    url(r'^add_lfg/(?P<pk>\d+)/$', views.AddLFG.as_view()), # by assignment
    url(r'^add_lfg/(?P<pk>\d+)/$', views.AddLFG.as_view()), # by assignment
    url(r'^put_lfg/$', views.PutLFG.as_view()), # by assignment
    # url(r'^add_lfm/$', views.AddLFM.as_view()),
    url(r'^add_thing/$', views.AddThing.as_view()),
    url(r'^questions/$', views.QuestionView.as_view()),
    url(r'^questions/(?P<which_ass>\d+)$', views.QuestionView.as_view()),
    url(r'^question/(?P<pk>\d+)$', views.QuestionDetailView.as_view()),
    url(r'^answer/(?P<question>\d+)/(?P<user>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.AnswersView.as_view()),
    url(r'^answer/$', views.AnswersView.as_view()),
    url(r'^recommend_team/$', views.TeamRecommend.as_view()),
    url(r'^recommend_student/$', views.StudentRecommend.as_view()),
    url(r'^add_project_pref/$', views.PutProjectPref.as_view()),

    # Add project
    url(r'^add_project/$', views.AddProject.as_view()),

    # Query projects by ass
    url(r'^projects/(?P<which_ass>\d+)/$', views.ProjectView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
