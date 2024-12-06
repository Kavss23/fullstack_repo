from django.urls import re_path,path
from users import views
from .views import validate_user

urlpatterns=[
    re_path(r'^api/users$',views.user_list),
    path('validate',views.validate_user),

    re_path(r'^api/users/(?P<pk>[0-9]+)$',views.user_details)

]