from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
   (r'^accounts/', include('allauth.urls')),
    # Examples:
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^contact/$', 'contact.views.home', name='contact'),
    url(r'^about/$', 'profiles.views.about', name='about'),
    url(r'^profile/$', 'profiles.views.user_profile', name='profile'),
    url(r'^checkout/$', 'checkout.views.checkout', name='checkout'),



    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
