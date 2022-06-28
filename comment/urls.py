from django.urls import path
from comment import views

urlpatterns = [
    path('comments/', views.comment, name='comment_view'),

]
