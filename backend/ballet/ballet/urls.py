from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ballet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dashboard/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^',include('home.urls')),
    #url(r'^perfiles/',include('perfiles.urls')),
    url(r'^diccionario/',include('diccionario.urls')),
    url(r'^cultura/',include('cultura.urls')),
    url(r'^avisos/',include('avisos.urls')),
    #url(r'^calendario/',include('calendario.urls')),
)


urlpatterns+=patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,} ),
)


urlpatterns+=patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS,} ),
)
