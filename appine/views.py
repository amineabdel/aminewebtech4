from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
# Create your views here.

import os
import json


def index(request):
    file = "appine/txtfile/infractions.json"
    with open(file) as fp:
        data = json.loads(fp.read())
        # print(data)
        context = {
            'infractions': data
        }
        data.sort(key=lambda s: s["infractions_speed"])

        return render(request, 'sjabloon/index.html', context)


def infractions(request, numbers):
    file = "appine/txtfile/infractions.json"
    with open(file) as fp:
        data = json.loads(fp.read())
        inteke = int(numbers)
        # print(inteke)
        speed = []
        for d in data:
            appendke1 = speed.append(d['infractions_speed'])
            data.sort(key=lambda s: s["infractions_speed"])
        print(d)
        x = [x for x in speed if x >= inteke]
        context = {
            'speed': x
        }

        return render(request, 'sjabloon/infra.html', context)


# def infractions(request, numbers):
#     file = "appine/txtfile/infractions.json"
#     with open(file) as fp:
#         data = json.loads(fp.read())
#         inteke = int(numbers)
#         # print(inteke)
#         speed = []
#         for d in data:
#             appendke1 = speed.append(d['infractions_speed'])
#             data.sort(key=lambda s: s["infractions_speed"])
#         print(d)
#         x = [x for x in speed if x >= inteke]
#         context = {
#             'speed': x
#         }

#         return render(request, 'sjabloon/infra.html', context)
