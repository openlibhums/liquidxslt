from django.urls import re_path

from plugins.liquidxslt import views


urlpatterns = [
    re_path(r'^manager/$', views.manager, name='liquidxslt_manager'),
    re_path(r'^edit/(?P<xsl_file_id>\d+)/$', views.edit_xslt_file, name='liquidxslt_edit_xslt_file'),
]
