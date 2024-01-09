from django.urls import path 
from .views import list ,post, add_comment

urlpatterns = [
    path('', list, name="list"),
    path('<int:id>', post, name="post"),
    path('add-comment/<int:id>/', add_comment, name='add_comment'),
]