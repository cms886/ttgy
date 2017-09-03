from  django.conf.urls import  url
from django.contrib import admin
from . import views
app_name = 'df_order'
urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'^place/$',views.place,name="placr"),
    url(r'^submit/$',views.placeSubmit,name="submit"),
]