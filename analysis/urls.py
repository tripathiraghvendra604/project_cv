from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^home$', views.home, name='home'),
    url(r'^education$', views.education, name='education'),

]