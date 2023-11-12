"""
URL configuration for dlesson6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from library1.views import (show_start_page, show_addrent_page, show_addreader_page, show_addbook_page, show_showbooks_page, show_showrents_page, show_showreaders_page,
                            show_deletebook_page,show_deleterent_page,show_deletereader_page,updateBook)

urlpatterns = [
    path('', show_start_page),
    path('showbooks/', show_showbooks_page),
    path('addbook/', show_addbook_page),
    path('addreader/', show_addreader_page),
    path('addrent/', show_addrent_page),
    path('showRents/', show_showrents_page),
    path('showReaders/', show_showreaders_page),
    path('delRent/', show_deleterent_page),
    path('delReader/', show_deletereader_page),
    path('delBook/', show_deletebook_page),
    path('showbooks/<int:pk>/', updateBook),
    path('admin/', admin.site.urls),
]
