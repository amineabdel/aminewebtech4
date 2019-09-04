from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
# Create your views here.

import os
import redis

url_list = []

r = redis.StrictRedis('localhost', 6379, db=0,
                      charset="utf-8", decode_responses=True)


def index(request):
    return HttpResponse("amine abdel")


# def detail(request, numbers):
#     urlsplit = [int(x) for x in numbers.split("/")]
#     som = sum(urlsplit)

#     path = request.path
#     appine = request.path.split("/")[1]
#     a = request.path.split("/")[2]
#     b = request.path.split("/")[3]
#     c = request.path.split("/")[4]
#     d = request.path.split("/")[5]

#     for item in request.path.split("/"):
#         url_list.append(item)
#         if item == '' or item == "appine":
#             url_list.remove(item)
#     print(url_list)

    # return HttpResponse("%d" % url_list)

    # print(url_list)
    # return HttpResponse("weed")


# def urlke(request):
#     s = ''
#     add_url(request)
#     for entry in url_list:
#         s += entry + '<br/>'

#     return HttpResponse(s)


# def add_url(request):
#     path = request.path
#     print(path)
#     if '//' not in path:
#         s = ''
#         temp = ""
#         while path != '/':
#             temp = os.path.split(path)
#             path = temp[0]
#             if temp[1] != 'urlparts':
#                 s += temp[1] + '---'

#         url_list.append(s)

# def rediske(request):
#     file = "appine/txtfile/movies.txt"

#     with open(file) as f:
#         for line in f:
#             movie = line.split(":")[1]
#             actors = line.split(":")[1]
#             # print(line.split(":")[0])
#             # print(line.split(":")[2])
#             # conv = line.split(':')[:1]
#             setke = r.hset("data", movie, actors)
#             getke = r.hgetall("data")
#             print(getke)

#             context = {
#                 "movie": getke,
#                 "actor": getke
#             }
#             return render(request, "sjabloon/index.html", context)

#             for item in getke:
#                 context = {
#                     "movie": item,
#                     "actor": r.hget('data', item)
#                 }
#                 return render(request, "sjabloon/index.html", context)
#     #return HttpResponse("weed")


# def oef(request):
#     module_dir = os.path.dirname(__file__)
#     file_path = os.path.join(module_dir, 'txtfile/movies.txt')
#     data_file = open(file_path, 'r')
#     for line in data_file:
#         movie = line.split(":")[:1]
#         actors = line.split(":")[1]
#         # print(actors)
#         setke = r.hset("movie", line, line)
#         getke = r.hgetall("movie")
#         context = {
#             "movie": getke,
#             "actor": getke
#         }
#         return render(request, "sjabloon/index.html", context)

#     # return HttpResponse("weed")


# def test(request):
#     r.set("name", "amine")
#     return HttpResponse("weed")
