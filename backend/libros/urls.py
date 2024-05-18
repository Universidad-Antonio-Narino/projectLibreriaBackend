from rest_framework import routers #crea las routas automaticamente
from .api import LibrosViewSet

#ejecuto los routers
router = routers.DefaultRouter()

router.register('api/libros',LibrosViewSet,'libros')


urlpatterns = router.urls