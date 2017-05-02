from django.conf.urls import url

from . import views
#matcher/questions
#matcher/question/<id>
#matcher/matches/<uid>
#user/
#user/answers/list
#user/answers/<id>
#
# url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
# url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions/$', views.QuestionListView.as_view(), name = "questions" ),
    url(r'^question/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question-detail'),
]