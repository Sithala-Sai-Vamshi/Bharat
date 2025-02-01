# urls.py
from django.urls import path
from .views import FAQListView, FAQDetailView

urlpatterns = [
    path('api/faqs/', FAQListView.as_view(), name='faq-list'),  
    path('api/faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'), 
]
