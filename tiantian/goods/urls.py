from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'goods'
urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'^$',views.index,name="index"),
    url('^detail/(?P<id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^list/(?P<pIndex>[0-9]+)/$',views.goodslist,name='goodslist'),
    url(r'^typelist/(?P<typeid>[0-9]+)/$',views.typelist,name='typelist'),
]
