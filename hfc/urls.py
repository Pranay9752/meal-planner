from django.urls import include, path

urlpatterns = [
    path('', include('hfc.api.urls')),
]