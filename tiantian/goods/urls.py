from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'goods'
urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'^$',views.index,name="index"),
    # url('^de/$',views.detail,name='detail'),
    url('^detail/(?P<id>[0-9]+)/$',views.detail,name='detail'),
]
