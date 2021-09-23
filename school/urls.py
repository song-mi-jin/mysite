from django.urls import path
from school import views


app_name = 'school'
urlpatterns = [
    path('', views.index, name='index'),
    ## 학생 리스트
    path('<int:student_id>/detail/', views.detail, name='detail'),
    ## 학생이 등록한 과목 리스트
    path('add/', views.add, name='add'),
    ## 학생 등록 처리
    path('<int:student_id>/update/', views.update, name='update'),
    ## 학생 정보 삭제
    path('<int:student_id>/remove/', views.remove, name='remove'),
    ## 과목 등록
    #path('<int:student_id>/sub_add/', views.sub_add, name='sub_add'),
    path('sub_add/', views.sub_add, name='sub_add'),
    ## 과목 수정
    path('<int:subject_id>/sub_add/', views.sub_add, name='sub_add'),
    ## 과목 삭제ㅐ
    path('<int:subject_id>/sub_del/', views.sub_del, name='sub_del'),    
    
]
