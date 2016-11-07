from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'water.views.index', {'a': '123'}),
    url(r'^index/$', 'views.index', {'a': '123'}, 'new_name', 'water'),
    url(r'test/\d{2}/$','water.views.test')
]



