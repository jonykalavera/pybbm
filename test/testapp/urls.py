from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('')


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            "show_indexes":True,
    }),
    (r'^', include('pybb.urls', namespace='pybb')),
    (r'^accounts/', include('registration.urls')),
    

)
