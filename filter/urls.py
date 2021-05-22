from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('movies/',views.movie,name="movie"),
    path('filter/',views.filter,name="filter"),
    path('filter/director/',views.filterD,name="filterdirector"),
    path('filter/director/<int:id>',views.directormovies,name="dmovies"),
]