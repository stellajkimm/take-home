from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'take_home_challenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('athletes.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
