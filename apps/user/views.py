from django.shortcuts import render, HttpResponse
from faker import Faker
# Create your views here.


def login(requset):
    fake = Faker(locale='zh_CN')
    return HttpResponse(fake.name()+"访问了")
