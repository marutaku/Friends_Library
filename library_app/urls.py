from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name = 'library_app'
urlpatterns = [
    url(r'^$', login,{'template_name': 'library_app/login.html'}, name='login'),
    url(r'^signup$', views.AccountCreateView.as_view(), name='signup'),
    url(r'^index$', views.RequestIndexView.as_view(), name='index'),
    url(r'^indexp$', views.PresentIndexView.as_view(), name='present_index'),
    url(r'^request$', views.request_page, name='request_page'),
    url(r'^present$', views.present_page, name='present_page'),
    url(r'^request/search_isbn$', views.search_isbn_request, name='search_isbn_request'),
    url(r'^present/search_isbn$', views.search_isbn_present, name='search_isbn_present'),
    url(r'^request/search_title$', views.search_title, name='search_title'),
    url(r'^request/regists$', views.regist_request, name='regist_request'),
    url(r'^present/regists$', views.regist_present, name='regist_present'),
    url(r'^index/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^delete$', views.request_delete, name='delete'),
    ]