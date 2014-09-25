from django.conf.urls import patterns, url, include

urlpatterns=patterns('perfiles.views',
	url(r'^$','index_view', name='perfiles'),
	url(r'^(?P<usuario>[\w\-]+)/$','usuario_perfil' ),
)