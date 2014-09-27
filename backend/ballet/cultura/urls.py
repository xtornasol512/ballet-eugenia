from django.conf.urls import patterns, url, include

urlpatterns=patterns('cultura.views',
    url(r'^$','index_view', name='posts'),
    url(r'^tag/','busqueda_post'),
    url(r'^tag/(?P<tag>[\w\-]+)/$','tag_post'),
    url(r'^(?P<post>[\w\-]+)/$','post'),
)