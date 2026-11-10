from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BarberViewSet, ServiceViewSet, AppointmentViewSet, PaymentViewSet, whatsapp_webhook

router = DefaultRouter()
router.register(r"barbers", BarberViewSet, basename="barber")
router.register(r"services", ServiceViewSet, basename="service")
router.register(r"appointments", AppointmentViewSet, basename="appointment")
router.register(r"payments", PaymentViewSet, basename="payment")

urlpatterns = router.urls + [
    path("whatsapp/webhook/", whatsapp_webhook, name="whatsapp-webhook"),
]
