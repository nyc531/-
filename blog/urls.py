from django.urls import path
from django.views.generic import TemplateView
from .views import ViweDetail
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('<int:pk>/', ViweDetail.as_view()),
    path('opss/', TemplateView.as_view(template_name='ops.html'))
]