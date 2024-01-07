from rest_framework import routers

from .viewsets import *

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'posts', PostsViewSet, 'posts')


urlpatterns = router.urls
