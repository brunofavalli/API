from django.conf.urls import patterns, include, url
from whatever.api import WhateverResource

whatever_resource = WhateverResource()

urlpatterns = patterns('',
   url(r'^api/', include(whatever_resource.urls)),
)

