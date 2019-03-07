"""airbus_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cms import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^get_feed/', views.get_feed),
    url(r'^get_feed_for_id/', views.get_feed_for_id),
    url(r'^get_aircraft_mode_for_id/', views.get_aircraft_model_for_id),
    url(r'^get_aircraft_for_id/', views.get_aircraft_for_id),
    url(r'^get_airport_for_id/', views.get_airport_for_id),
    url(r'^get_flight_for_id/', views.get_flight_for_id),
    url(r'^get_aircraft_models/', views.get_aircraft_models),
    url(r'^get_aircraft_for_msn/', views.get_aircraft_for_msn),
    url(r'^get_all_flights_for_msn/', views.get_all_flights_for_msn),
    url(r'^get_all_flights_for_msn_filter/', views.get_all_flights_for_msn_filter),
    url(r'^get_flight_info/', views.get_flight_info),
]
