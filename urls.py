from django.conf.urls import url

from plugins.liquidxslt import views


urlpatterns = [
    url(r'^manager/$', views.manager, name='liquidxslt_manager'),
    url(r'^edit/(?P<xsl_file_id>\d+)/$', views.edit_xslt_file, name='liquidxslt_edit_xslt_file'),
]
