from django.conf.urls import url
from api import views
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

category_list = views.CategoryViewSet.as_view({
    'get':'list',
    'post' :'create'
})

category_detail = views.CategoryViewSet.as_view({
    'get':'retrieve'
})

status_list = views.StatusViewSet.as_view({
    'get':'list',
    'post':'create'
})


urlpatterns = format_suffix_patterns( [
    url(r'^api/category/$', category_list, name='category-list'),
    url(r'^api/category/(?P<pk>[0-9]+)/$', category_detail, name='category-detail'),
    url(r'^api/$', views.api_root),
    #url(r'^api/publications/$', views.PublicationList.as_view()),
    url(r'^api/status/$', status_list, name='status-list'),
])
