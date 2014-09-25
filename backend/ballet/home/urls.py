from django.conf.urls import patterns, url, include

urlpatterns=patterns('home.views',
	url(r'^$','index_view', name='index'),
	url(r'^missgennyta/','missgennyta'),
	url(r'^contacto/','contacto'),
	url(r'^reglamento/','reglamento'),
	url(r'^login/','login'),
)