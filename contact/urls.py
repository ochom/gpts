from django.urls import path

from contact import views

urlpatterns = [
    path('', views.render_landing_page),
    path('error', views.render_error_page),
    path('success', views.render_success_page),
    path('contactus/api', views.contact_us),
    path('subscribe/api', views.subscribe)
]