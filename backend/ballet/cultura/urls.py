from django.conf.urls import patterns, url, include

urlpatterns=patterns('cultura.views',
	url(r'^$','index_view', name='cultura'),
	url(r'^(?P<aviso>[\w\-]+)/$','aviso'),
	url(r'^tag/(?P<aviso>[\w\-]+)/$','tag_aviso'),
)