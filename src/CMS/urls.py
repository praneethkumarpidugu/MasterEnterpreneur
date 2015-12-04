from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    #url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='home'),
    #url(r'^pricing/$', TemplateView.as_view(template_name='pricing.html'), name='home'),
    #url(r'^contact_us/$', TemplateView.as_view(template_name='pricing.html'), name='home'),
    url(r'^$', 'CMS.views.home', name='home'),
    url(r'^staff/$', 'CMS.views.staff_home', name='staff'),
    # url(r'^about/about/about/', 'CMS.views.home', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#auth login/logout
urlpatterns += patterns(
    'CMS.views',
    url(r'^login/$', 'auth_login', name='login'),
    url(r'^logout/$', 'auth_logout', name='logout'),

)
