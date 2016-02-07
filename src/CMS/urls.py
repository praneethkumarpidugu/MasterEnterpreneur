from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    #url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='home'),
    #url(r'^pricing/$', TemplateView.as_view(template_name='pricing.html'), name='home'),
    url(r'^contact_us/$', TemplateView.as_view(template_name='pricing.html'), name='contact_us'),
    url(r'^$', 'CMS.views.home', name='home'),
    url(r'^staff/$', 'CMS.views.staff_home', name='staff'),
    # url(r'^about/about/about/', 'CMS.views.home', name='about'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^videos/$', 'videos.views.category_list', name="category_list"),
    url(r'^videos/(?P<cat_slug>[\w-]+)/$', 'videos.views.category_detail', name="category_detail"),
    url(r'^videos/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', 'videos.views.video_detail', name="video_detail"),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += patterns('',) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += patterns('billing.views',
    url(r'^upgrade/$', 'upgrade', name='account_upgrade'),
    url(r'^billing/$', 'billing_history', name='billing_history'),
)

#auth login/logout
urlpatterns += patterns(
    'accounts.views',
    url(r'^login/$', 'auth_login', name='login'),
    url(r'^logout/$', 'auth_logout', name='logout'),
    url(r'^register/$', 'auth_register', name='register'),
    #If you wanted to have just paid users remove the above auth_register
    #currently we have free and paid users
)

#comment thread
urlpatterns += patterns(
    'comments.views',
    url(r'^comment/(?P<id>\d+)$', 'comment_thread', name='comment_thread'),
    url(r'^comment/create/$', 'comment_create_view', name='comment_create'),

)
urlpatterns += patterns(
    'notifications.views',
    url(r'^notifications/$', 'all', name='notifications_all'),
    url(r'^notifications/ajax/$', 'get_notifications_ajax', name='get_notifications_ajax'),
    url(r'^notifications/(?P<id>\d+)/$', 'read', name='notifications_read'),
)
