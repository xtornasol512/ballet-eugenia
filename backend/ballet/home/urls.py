from django.conf.urls import patterns, url, include

urlpatterns=patterns('home.views',
	url(r'^$','index_view', name='index'),
	url(r'^missgennita/','missgennita'),
    url(r'^calendario/', 'calendario'),
	url(r'^contacto/','contacto'),
    url(r'^academia/','academia'),
	url(r'^reglamento/','reglamento'),
	url(r'^login/','login'),
)