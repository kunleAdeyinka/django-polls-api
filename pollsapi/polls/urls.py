from posixpath import basename
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .apiviews import PollViewSet
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path to the login endpoint
    path("login/", views.obtain_auth_token, name="login"),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    # connects the User Serializer to the urls.py
    path("users/", UserCreate.as_view(), name="user_create"),
]

urlpatterns += router.urls