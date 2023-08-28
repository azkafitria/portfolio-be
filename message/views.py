from django.shortcuts import render
from .models import *
import json

# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed


def send_message(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))
    try:
        data = json.loads(request.body)
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        message = Message(name=name, email=email, phone=phone, message=message)
        message.save()
        return HttpResponse(json.dumps({"status": 400, "message": "OK"}), content_type="application/json")
    except KeyError:
        return HttpResponseBadRequest(json.dumps({"status": 400, "message": "Bad request"}), content_type="application/json")