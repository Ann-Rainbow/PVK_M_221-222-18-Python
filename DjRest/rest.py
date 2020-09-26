from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

def dictToStr(dictionary):
    retStr = ""
    for item in dictionary:
        retStr += f"{str(item)} : {str(dictionary.get(item))}\n"
    return retStr

@csrf_exempt # отключение csrf
def rest_request(request):
    str1 = ""
    if request.method == "GET":
        str1 = "GET parameters: " + dictToStr(request.GET)
    if request.method == "POST":
        str1 += "<br>POST Data:<br>"
        str1 += dictToStr(json.loads(request.body))
    return HttpResponse(str1)
