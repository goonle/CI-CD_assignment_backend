from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet, NoteCreateView

# router = DefaultRouter()
# router.register(r'notes', NoteViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path('create/', NoteCreateView.as_view(), name='create'),
]

