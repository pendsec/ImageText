"""External urls."""
from django.urls import path

from . import views

app_name = "external"
urlpatterns = [
    path('home', views.ImagetextLandingView.as_view(), name='landing-page'),
    path('predict', views.PredictView.as_view(), name='predict'),
    path('output', views.OutputView.as_view(), name='output')
]
