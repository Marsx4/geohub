
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name="site_home"),
    path('detail/<slug:organization>/',views.detail,name="org_detail"),
]
