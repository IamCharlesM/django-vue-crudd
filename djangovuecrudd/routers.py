from rest_framework import routers
from article.viewset import ArticleViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)