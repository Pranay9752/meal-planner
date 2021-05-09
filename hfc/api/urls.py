from django.urls import include, path
from .views import RecommendFoodView
from django.conf.urls import url

urlpatterns = [
    url(r'^api/$', RecommendFoodView.as_view(), name='recommend_food'),
]