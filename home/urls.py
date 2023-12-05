

from django.urls import path
from .views import(
    index,
    create_blog,
    updateblog
)
urlpatterns = [

    path('',  index ),
    path('create/', create_blog),
    path('update/<int:id>', updateblog)
]
