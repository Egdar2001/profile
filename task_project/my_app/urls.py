
from django.urls import path
from . import views

urlpatterns = [

    path("",views.createProfile),

    path("",views.ListView.as_view(),name='profilelist'),

    path('detailview/<int:profile_id>/',views.detailsview,name='details'),

    path('updateview/<int:profile_id>/',views.updateprofile,name='update'),

    path('deleteview/<int:profile_id>/',views.deleteView,name='delete')






]
