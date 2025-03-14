from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet, NoteCreateView, NoteListView

# router = DefaultRouter()
# router.register(r'notes', NoteViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path('create/', NoteCreateView.as_view(), name='create'),
    path('retrieve/', NoteListView.as_view(), name='retrieve'),
]

