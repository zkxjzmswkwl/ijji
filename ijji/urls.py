from django.contrib import admin
from django.urls import include, path

from vods.api import VodList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/diceroll/vods/", VodList.as_view()),
]
