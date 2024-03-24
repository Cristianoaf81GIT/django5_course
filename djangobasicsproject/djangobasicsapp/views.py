#pyright: reportUnusedVariable=false
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest 
from datetime import datetime
import logging

# Create your views here.

def Home(_request: HttpRequest) -> HttpResponse:
    return HttpResponse(b"<h1>Hello from django 5.0</h1>")

def ShowMoreMessage(_request: HttpRequest) -> HttpResponse:
     return HttpResponse(b"<h1>Hello from django 5.0</h2><h1>Hello from django 5.0</h2><h3>Hello from django 5.0</h3><h4>Hello from django 5.0</h4><h5>Hello from django 5.0</h5><h6>Hello from django 5.0</h6>")

def UseVariableAsResponse(_request: HttpRequest) -> HttpResponse:
    #print(_request.headers)    
    Message = "<h1>Welcome to django development.</h1>"
    Message += "<h2>Welcome to django development.</h2>"
    Message += "<h3>Welcome to django development.</h3>"
    Message += "<h4>Welcome to django development.</h4>"
    Message += "<h5>Welcome to django development.</h5>"
    Message += "<h6>Welcome to django development.</h6>"
    return HttpResponse(Message.encode())

def GetRequestVariables(request: HttpRequest) -> HttpResponse:
    user_agent = request.META['HTTP_USER_AGENT']
    Message = user_agent if len(user_agent) > 0 else "" 
    if request.method == 'GET' and request.GET.get('Message'):
        Message += f"<h1>{str(request.GET.get('Message'))}</h1>"
    else:
        Message += "<h1>You havent supplied value for Message parameter...</h1>"

    if request.method == 'GET' and request.GET.get('Country'):
        Message += f"<h1>{str(request.GET.get('Country'))}</h1>"
    else:
        Message += "<h1>You havent supplied value for Country parameter...</h1>"

    return HttpResponse(Message.encode())
        

def ShowDateTimeInfo(request: HttpRequest) -> HttpResponse:
    todays_date = datetime.now()
    template_file_name = 'djangobasicsapp/ShowTimeInfo.html'
    context: dict = { 'TodaysDate': todays_date }
    return render(request=request,template_name=template_file_name,context=context)

def LoggingExample(_request: HttpRequest) -> HttpResponse:
    filelogger = logging.getLogger('filelogger')
    filelogger.debug(f"debug: I justentered into the view ... {datetime.now()}")
    filelogger.info("Info: Confirmation that the things are working as expected")
    filelogger.warning("Warning: An indication that something unexpected happened")
    filelogger.error("Error: Due to more serious problems the software does not be able to exec something") 
    filelogger.critical("Critical: A serius error, that eventualy can causes crash on application")
    return HttpResponse('ok'.encode())
