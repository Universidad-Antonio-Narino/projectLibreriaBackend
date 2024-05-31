from rest_framework import routers #crea las routas automaticamente
from .views import *
from django.contrib import admin



#ejecuto los routers
router = routers.DefaultRouter()

router.register('api/libros',LibrosViewSet,'libros')
router.register('api/transaccion',TransaccionViewSet,'transacciones')


urlpatterns = router.urls