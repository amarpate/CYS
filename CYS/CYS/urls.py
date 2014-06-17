from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mailer.views.home', name='home'),
    url(r'^thank-you/$', 'mailer.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'mailer.views.aboutus', name='aboutus'),
    url(r'^more-info/$', 'mailer.views.more', name='more'),
   	# url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, 
					document_root=settings.STATIC_ROOT)

	urlpatterns += static(settings.MEDIA_URL, 
					document_root=settings.MEDIA_ROOT)