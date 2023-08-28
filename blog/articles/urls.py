from django.urls import path
from . import views

urlpatterns = [path('<str:pagename>', views.ArticleView.as_view(), name='get'),
               path('section/<str:section>', views.SectionView.as_view(), name='section'),
               path('', views.SectionView.as_view(), {'section' : 'home'}, name='home')
               ]