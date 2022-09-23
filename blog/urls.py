# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:12:29 2022

@author: cfmar
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list')]