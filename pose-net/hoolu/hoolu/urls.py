from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'hoolu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('water.urls')),
    # url(r'^index$', 'water.views.index', name='index'),
    # url(r'^$', 'water.views.index', name='index'),
]
