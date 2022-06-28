from django.contrib import admin
from django.urls import path 
from firstpage import views


urlpatterns = [
    path("",views.index,name='HomePage'),
    path("predictCovid",views.predictCovid,name='predictCovid'),
    path("predictions",views.predictions,name='predictions'),
    path("HomePage",views.index,name='HomePage'),
    ########## Experiment ##########
    #path("explore",views.show_explore_page,name='explore')
]