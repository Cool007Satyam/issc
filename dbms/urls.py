from django.conf.urls import include,url
#from django.contrib import admin
import views,models


urlpatterns=[
       #url(r'^$',include(dbms.urls)
       url(r'^export/',views.ExportSubtask),
       url(r'^done/(?P<tid>\d+)/(?P<res>\d+)/$',views.GetData),
       url(r'^download/',views.Download)

]
