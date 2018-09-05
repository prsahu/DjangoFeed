from rest_framework import routers
from .viewsets import ArticleViewSet
from .views import ArticleViewSet as AP

router = routers.DefaultRouter()
router.register(r'feeds', ArticleViewSet)
# router.register(r'song/create',AP)

# for url in router.urls:
#     print(url)