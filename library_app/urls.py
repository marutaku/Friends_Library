from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name = 'library_app'
urlpatterns = [
    url(r'^$', login,{'template_name': 'library_app/login.html'}, name='login'),
    url(r'^signup$', views.AccountCreateView.as_view(), name='signup'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^request$', views.request_page, name='request_page'),
    url(r'^request/search_isbn$', views.search_isbn, name='search_isbn'),
    url(r'^request/search_title$', views.search_title, name='search_title'),
    url(r'^request/regists$', views.regist_book, name='regist_request'),
    url(r'^index/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    ]