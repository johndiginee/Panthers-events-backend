from django.urls import path
import views


urlpatterns = [
    path('events/', views.CreateAPIView.as_view(), name='create-event'),
    path('events/<int:id>/', views.RetrieveAPIView.as_view(), name='event-detail'),
    path('events/', views.EventListAPIView.as_view(), name='event-list'),

    path('api/users/<int:userId>/interests/<int:eventId>/', views.ExpressInterestView.as_view(),
         name='express-interest')
]
