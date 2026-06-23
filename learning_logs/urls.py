from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all Topics
    path('topics/', views.topics, name='topics'),
    # Details page for an individual topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

]