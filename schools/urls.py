from django.urls import path
from . import views

app_name ='schools'
 
urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    #SCHOOL_VIEWS
    path('',views.SchoolListView.as_view(),name='school_list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name='std_detail'), #std <int:sk>/<int:pk>/
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.SchoolDeleteView.as_view(),name='delete'),
    #STUdent
    path('std_create/',views.StudentCreateView.as_view(),name='std_create'), 
    # we made this create student in public because user will chooses school when adding student
    # we will try to add a button in every school to add student in this school only url will be something like this 
    # '1/create_std/<int:pk>'
    path('update_std/<int:pk>',views.StudentUpdateView.as_view(),name='std_update'), # we need to write pk of school at begin
    path('std_delete/<int:pk>',views.StudentDeleteView.as_view(),name='std_delete'),
    




    
]