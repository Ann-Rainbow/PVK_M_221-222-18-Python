from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

def dictToStr(dictionary):
    resultStr = ""
    for item in dictionary:
        resultStr += f"{str(item)} : {str(dictionary.get(item))}\n"
    return resultStr

@csrf_exempt # отключение csrf
def rest_request(request):
    inputData = ""
    if request.method == "GET":
        inputData = "GET parameters: " + dictToStr(request.GET)
    if request.method == "POST":
        inputData += "<br>POST Data:<br>"
        inputData += dictToStr(json.loads(request.body))
    return HttpResponse(inputData)
