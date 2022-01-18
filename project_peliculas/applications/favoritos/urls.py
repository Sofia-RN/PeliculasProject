
from django.urls import path, re_path

from . import views

app_name = 'fav_app'

urlpatterns = [
    path(
        'api/reuniones-link/',
        views.ReunionApiListaLink.as_view(),
    ),

]