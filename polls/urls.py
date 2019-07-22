from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index),  # views.py 안에 index 함수 호출
    # ctrl + 마우스 커서 하면 지정된 곳으로 이동 가능

    path('', views.index, name='index'),      # /polls/
    path('<int:question_id>/', views.detail, name='detail'),       # /polls/5/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # /polls/5/vote/
    path('<int:question_id>/results/', views.results, name='results'),     # /polls/5/results/

]
