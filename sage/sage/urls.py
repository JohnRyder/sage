from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from accounts.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^authentication/', include('allaccess.urls')),
    url(r'^api/v1/', include(router.urls))
    #url('^.*$', IndexView.as_view(), name='index'),
)
