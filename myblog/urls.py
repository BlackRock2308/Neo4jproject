from django.urls import path
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("dashboard/", home, name="dashboard" ),
    path("post/", get_article, name='article'),
    path('post/<int:pk>/', post_detail, name = 'post_detail'),
    path("articles/", get_article, name='article'),
    path("editer/", writearticle, name='editer_post')
   
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)