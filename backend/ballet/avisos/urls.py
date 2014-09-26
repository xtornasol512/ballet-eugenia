from django.conf.urls import patterns, url, include

urlpatterns=patterns('avisos.views',
    url(r'^$','index_view', name='avisos'),
    url(r'^tag/','busqueda_aviso'),
    url(r'^tag/(?P<tag>[\w\-]+)/$','tag_aviso'),
    url(r'^(?P<aviso>[\w\-]+)/$','aviso'),
)