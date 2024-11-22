from django.urls import path
from .views import CampaignListView, CampaignCreateView, CampaignUpdateView, CancelCampaignView, UserListView


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('campaign/', CampaignListView.as_view(), name='campaign-list'),
    path('campaign/create/', CampaignCreateView.as_view(), name='campaign-create'),
    path('campaign/<int:pk>/update/', CampaignUpdateView.as_view(), name='campaign-update'),
    path('campaign/<int:pk>/cancel/', CancelCampaignView.as_view(), name='campaign-cancel'),
]
