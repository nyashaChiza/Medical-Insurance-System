from django.urls import path

from .views import(
    
    # Urls service providers
    ServiceProviderListView,
    ServiceProviderCreateView,
    ServiceProviderUpdateView,
    ServiceProviderDeleteView,
    ServiceProviderDetailView
)

urlpatterns = [
    path('service-providers-index', ServiceProviderListView.as_view(),name = "service-providers-index"),
    path('create-service-provider', ServiceProviderCreateView.as_view(),name = "create-service-provider"),
    path('update-service-provider/<int:pk>/', ServiceProviderUpdateView.as_view(), name="update-service-provider"),
    path('delete-service-provider/<int:pk>/', ServiceProviderDeleteView.as_view(), name="delete-service-provider"),
    path('service-provider-details/<int:pk>/', ServiceProviderDetailView.as_view(), name="service-provider-details"),

]
