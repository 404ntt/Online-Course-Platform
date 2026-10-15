from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from api.views import ApiViews

jwtpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('api/courselist/', ApiViews.CourseApiListView.as_view(), name='CourseListApi'),
    path('api/courseretrieve/<int:pk>', ApiViews.CourseApiRetrieveView.as_view(), name='CourseRetrieveApi'),
    path('api/lessonlist/', ApiViews.LessonListApiView.as_view(), name='LessonListApi'),
    path('api/lessonretrieve/<int:pk>', ApiViews.LessonApiRetrieveView.as_view(), name='LessonRetrieveApi')
] + jwtpatterns

