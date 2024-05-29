from rest_framework import routers #crea las routas automaticamente
from .views import *

#ejecuto los routers
router = routers.DefaultRouter()

router.register('api/libros/admin',LibrosAdminViewSet,'libros')
router.register('api/transaccion',TransaccionViewSet,'transacciones')


urlpatterns = router.urls