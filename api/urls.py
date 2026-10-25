from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from api.views import ApiViews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'api/courselist', ApiViews.CourseApiViewset, basename='CourseApiView')
router.register(r'api/courseretrieve/', ApiViews.CourseApiView, basename='CourseRetrieve')

jwtpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', ApiViews.RegisterApiView.as_view(), name='register')
]

       

urlpatterns = [
    path('api/lessonlist/', ApiViews.LessonListApiView.as_view(), name='LessonListApi'),
    path('api/lessonretrieve/<int:pk>', ApiViews.LessonApiRetrieveView.as_view(), name='LessonRetrieveApi'),
    path('api/enrollmentlist/', ApiViews.EnrollmentApiListView.as_view(), name='EnrollmentList'),
] + jwtpatterns + router.urls

