from django.conf.urls import patterns, url, include

urlpatterns=patterns('diccionario.views',
	url(r'^$','index_view', name='avisos'),
	url(r'^(?P<palabra>[\w\-]+)/$','palabra'),
	url(r'^tag/(?P<palabra>[\w\-]+)/$','tag_palabra'),
)