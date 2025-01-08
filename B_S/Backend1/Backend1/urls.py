"""
URL configuration for Backend1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/singleAnalyze/', views.singleEmoAnalyze, name="singleEmoAnalyze"),
    path('api/provinceData/', views.wholeEmotionBar, name="wholeEmotionBar"),
    path('api/fileUpload/', views.fileUpload, name="fileUpload"),
    path('api/commentList/', views.getComment, name="getComment"),
    path('api/postURL/', views.getURL, name="getURL"),
    path('api/isAnalyzeFinished/', views.getWholeEmoAnalyze, name="getWholeEmoAnalyze"),
    path('api/isFileAnalyzeFinished/', views.getFileEmoAnalyze, name="getFileEmoAnalyze"),
    # path('api/comment_list/', views.getComment, name="getComment"),
]
