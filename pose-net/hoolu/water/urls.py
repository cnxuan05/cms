from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'water.views.index', {'a': '123'}),
    url(r'^index/$', 'views.index', {'a': '123'}, 'new_name', 'water'),
    url(r'test/\d{2}/$', 'water.views.test'),
    # url(r'test2/(?P<id>\d{2})/$', 'water.views.test2'),
    url(r'test2/', 'water.views.test2'),
    url(r'test3/(?P<id>\d{2})/(?P<key>\w+)/$', 'water.views.test3'),

    url(r'login/', 'water.views.login'),
    url(r'register/', 'water.views.register'),

url(r'test5/', 'water.views.test5'),
]
