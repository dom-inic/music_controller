from django.urls import path
from . import views
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

app_name = 'polls'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path("", views.polls_list, name="polls_list"),
    # path("polls/<int:pk>/", views.polls_detail, name="polls_detail")
    path("", PollList.as_view(), name="polls_list"), 
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"), 
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote", CreateVote.as_view(), name="create_vote"), 

] 
