from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from blog import views as blogViews
from users import views as userViews
from images import views as imageViews

app_name = 'api'

router = DefaultRouter()
router.register('articles', blogViews.ArticleViewSet)
router.register('comments', blogViews.CommentViewSet)
router.register('images', imageViews.ImagesViewSet)
router.register('profile', userViews.UserProfileViewSet)
router.register('tags', blogViews.TagViewSet)
router.register('login', userViews.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^articles/list/published/$', blogViews.ArticlePublishedList.as_view()),
]