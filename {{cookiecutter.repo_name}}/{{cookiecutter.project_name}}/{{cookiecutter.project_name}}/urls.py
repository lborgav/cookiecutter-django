from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    # Base, 404, 500 templates
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='base'),
    url(r'^404/$', TemplateView.as_view(template_name="404.html"), name='404'),
    url(r'^500/$', TemplateView.as_view(template_name="500.html"), name='500'),

    # Admin + AdminDocs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
