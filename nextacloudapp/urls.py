from rest_framework.routers import DefaultRouter
from nextacloudapp import views

router = DefaultRouter()
router.register(r'equipmentanditems', views.EquipmentAndItemsViewSet, basename='equipmentanditems')
router.register(r'brands', views.BrandsViewSet, basename='brands')
router.register(r'stores', views.StoreViewSet, basename='stores')


urlpatterns = router.urls