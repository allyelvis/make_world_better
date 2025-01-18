
from django.contrib import admin
from django.urls import path
from initiatives.views import InitiativeListView
from volunteers.views import VolunteerListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/initiatives/', InitiativeListView.as_view(), name='initiatives-list'),
    path('api/volunteers/', VolunteerListView.as_view(), name='volunteers-list'),
]

