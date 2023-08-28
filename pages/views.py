from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog, Adviser
from django.core.paginator import Paginator