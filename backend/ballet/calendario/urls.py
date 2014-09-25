from django.conf.urls import patterns, url, include

urlpatterns=patterns('calendario.views',
	url(r'^$','index_view', name='calendario'),
	url(r'^anual/','anual'),
	url(r'^mensual/','mensual'),
)