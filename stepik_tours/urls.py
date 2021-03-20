from django.urls import path

import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

import tours.views as tours_views

urlpatterns = [
    path("", tours_views.main_view, name="main"),
    path("departure/<str:departure>/", tours_views.departure_view,
         name="departure"),
    path("tour/<int:tour_id>/", tours_views.tour_view, name="tour"),
]

handler404 = tours_views.custom_handler404
handler500 = tours_views.custom_handler500

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
