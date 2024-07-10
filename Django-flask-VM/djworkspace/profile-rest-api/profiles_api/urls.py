from django.urls import include, path
from profiles_api import views
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('bookvs', views.BookViewSet, basename='bookvs')
router.register('empvs', views.EmpViewSet, basename='empvs')
router.register('profilevs', views.UserProfileViewSet)
router.register('feedvs', views.UserProfileFeedViewSet)


urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),
	path('books/', views.BookApiView.as_view()),
    path('emps/', views.EmpApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
