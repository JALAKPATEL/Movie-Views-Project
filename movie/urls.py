
from django.contrib import admin
from django.urls import path
from movie import views as movieViews

urlpatterns = [
    path('',movieViews.home,name='home'),
    path('about/',movieViews.about,name='about'),
    path('signup/',movieViews.signup,name='signup'),
    path('movie/<int:movie_id>',movieViews.detail,name='detail'),
    path('movie/<int:movie_id>/create',movieViews.createreview,name='createreview'),
    path('movie/review/<int:review_id>',movieViews.updatereview,name='updatereview'),
    path('movie/review/<int:review_id>/delete',movieViews.deletereview,name='deletereview'),
    
    
]
