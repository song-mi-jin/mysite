from django.urls import path
from polls import views
from polls.views import PollsListView

app_name = 'polls'

urlpatterns = [
    #path('', views.index, name='index'),      # /polls/
    path('', PollsListView.as_view(), name='index'),
    path('<int:question_id>/', views.detail, name='detail'),       # /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),     # /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # /polls/5/vote/
]
