from django.urls import path

from search.views import HomeView, SearchView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
]
