from django.conf.urls import url, include

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
    url(r'^questions/$', views.QuestionList, name ="questions" ),
    url(r'^question/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question'),
]
urlpatterns += [
    url(r'^myanswers/$', views.UserAnswersListView.as_view(), name='myanswers'),
]
urlpatterns += [
    url(r'^create/answers/$', views.AnswerInstanceView.as_view(), name='answer_view'),
    url(r'^create/question/$', views.QuestionInstanceView.as_view(), name='question_view'),
    #url(r'^answers/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    #url(r'^answers/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
urlpatterns += [
    url(r'^profile/edit/$', views.update_profile, name='profile_edit'),
]