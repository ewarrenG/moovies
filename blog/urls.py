from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^blog/$', views.index, name='index'), #hack
    url(r'^all/$', views.BlogListView.as_view(), name='blog-list'),
    #url(r'^all/$', views.MovieListView.as_view(), name='movie-list'),
    
    url(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),

    url(r'^bloggers/$', views.BlogAuthorListView.as_view(), name='blogauthor-list'),
    url(r'^blogger/(?P<pk>\d+)$', views.BlogAuthorDetailView.as_view(), name='blogauthor-detail'),

    #url(r'^books/$', views.BooksPage, name='books'),

]

