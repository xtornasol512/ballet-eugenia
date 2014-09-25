from django.conf.urls import patterns, url, include

urlpatterns=patterns('avisos.views',
	url(r'^$','index_view', name='avisos'),
	url(r'^(?P<aviso>[\w\-]+)/$','aviso'),
	url(r'^tag/(?P<aviso>[\w\-]+)/$','tag_aviso'),
)