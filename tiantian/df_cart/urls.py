
from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'df_cart'
urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'^gwc/$',views.gwc,name="gwc"),
    url(r'^showcar/$',views.showcar,name="showcar"),

    url(r'^$',views.cart),
    url(r'^add(\d+)_(\d+)/$',views.add),
    # url(r'^edit(\d+)_(\d+)/$',views.edit),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^addnum/$',views.addnum),

]