from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^send_notification/', 'gateway.services.send_notification_message'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
