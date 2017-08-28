
from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'df_cart'
urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'^gwc/$',views.gwc,name="gwc"),
]
