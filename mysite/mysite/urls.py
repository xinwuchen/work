from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^search/$',search),
    (r'^search/(\w+)/$',Books_information),
    (r'^edit/$',Edit),
    (r'^delete/$',Delete),
    (r'^$',Home),
    (r'^addA/$',addA),
    (r'^addB/$',addB),
    (r'^about/$',About),
    url(r'^admin/', include(admin.site.urls)),
)