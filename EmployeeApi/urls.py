from django.urls import path
from .views import Employee_Viewset, Department_Viewset, Computer_Viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', Employee_Viewset, base_name='Employee')
router.register('department', Department_Viewset, base_name='Department')
router.register('computer', Computer_Viewset, base_name='Computer')
router.register('training', Training_Viewset, base_name="Training")
urlpatterns = router.urls