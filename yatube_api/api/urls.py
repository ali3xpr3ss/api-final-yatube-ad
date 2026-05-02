from django.urls import include, path
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/api-token-auth/', auth_views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
