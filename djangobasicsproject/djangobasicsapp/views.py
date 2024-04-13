#pyright: reportUnusedVariable=false
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest 
from datetime import datetime
import logging
from typing import Any, TypedDict
from dataclasses import dataclass
import requests 
from pydantic import BaseModel
from djangobasicsapp.models import Authors

@dataclass
class Processors(TypedDict):
    Category: str
    processors: list[str]

@dataclass 
class Product(TypedDict):
    productID: int
    productName: str
    quantity: int
    unityStock: int
    disContinued: bool
    cost: float 

class User(BaseModel):
    address: dict[str, Any]
    id: int
    email: str
    username: str
    password: str
    name: dict[str, Any]
    phone: str    

@dataclass
class ProductContext(TypedDict):
    Products: list[Product]
    TotalOfProducts: int
    ProcessorsList: list[Processors] 


# Create your views here.

def Index(request) -> HttpResponse:
    return render(request, 'djangobasicsapp/Index.html')

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


def ifTagDemo(request: HttpRequest) -> HttpResponse:
    data: dict = dict({
        'name': 'Jimmy Anderson',
        'isVisible': True,
        'loggedIn': False,
        'countryCode': 'BR',
        'workingExperience': 5,
        'stateCode': 'Test'
    })

    template_file_name = 'djangobasicsapp/IfTagDemo.html'

    context: dict = dict({'Data': data})
    return render(request=request, template_name=template_file_name, context=context)

def ShowProducts(request: HttpRequest) -> HttpResponse:
    products: list[Product] = []
    products.append(
        {
            "productID": 1,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": False,
            "cost": 3000.0,
        }
    )
    products.append(
        {
            "productID": 2,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": False,
            "cost": 3000.0,
        }
    )
    products.append(
        {
            "productID": 3,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": False,
            "cost": 3000.0,
        }
    )
    products.append(
        {
            "productID": 4,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": False,
            "cost": 3000.0,
        }
    )
    products.append(
        {
            "productID": 5,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": False,
            "cost": 3000.0,
        }
    )
    products.append(
        {
            "productID": 6,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": True,
            "cost": 8000.0,
        }
    )
    products.append(
        {
            "productID": 7,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": True,
            "cost": 9000.0,
        }
    )
    products.append(
        {
            "productID": 8,
            "productName": "AMD Ryzen 3990",
            "quantity": 100,
            "unityStock": 5,
            "disContinued": True,
            "cost": 10000.0,
        }
    )
    
    ProcessorsList: list[Processors] = [
        {
            'Category': 'AMD', 
            'processors': [
                'Ryzen 3990',
                'Ryzen 3970',
                'Ryzen 3960',
                'Ryzen 3950'
            ], 
        },
        {
            'Category': 'Intel',
            'processors': [
                'Xeon 8362',
                'Xeon 8358',
                'Xeon 8380'
            ]        
        },
    ]

    template_file_name = 'djangobasicsapp/ShowProducts.html'
    
    context: ProductContext = {
        "Products": products,
        "TotalOfProducts": len(products),
        "ProcessorsList": ProcessorsList
    }

    return render(request=request, template_name= template_file_name, context=context)

def LoadUsers(request: HttpRequest) -> HttpResponse:
    templatefilename = 'djangobasicsapp/ShowUsers.html'
    response = CallRestApi()
    context: dict[str, list[User]] = {"users": response.json()}
    return render(request=request, template_name=templatefilename, context=context)

def LoadUsers2(request: HttpRequest) -> HttpResponse:
    templatefilename = 'djangobasicsapp/ShowUsersAsCard.html'
    image = 'https://i.pravatar.cc'
    response = CallRestApi()
    context: dict[str, list[User] | str] = {"users": response.json(),"image": image}
    return render(request=request, template_name=templatefilename, context=context)

def CallRestApi() -> requests.Response:
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users')
    return response

def CallRestApi2(userid: int) -> requests.Response:
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users/{userid}')
    return response

def LoadUserDetails(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':
        new_user_id: str = request.POST.get(key='useridcounter', default='11') or '11' #pyright: ignore
        counter = int(new_user_id)
        if request.POST.get('btnNext'):
            counter = counter + 1
            if counter > 11:
                counter = 1
        elif request.POST.get('btnPrevius'):
            counter = counter - 1
            if counter == 0:
                counter = 1
    else:        
        counter = 1
        
    templatefilename = 'djangobasicsapp/ShowUserDetails.html'
    response = CallRestApi2(counter)
    image = 'https://i.pravatar.cc'
    context: dict[str, User | str] = {
        "user": response.json(), 
        "image": image
    }
    return render(request, templatefilename, context)

def pass_model_2_template(request: HttpRequest) -> HttpResponse:
    # instattiate authors model 
    authors: list[Authors] = []
    authors.append(Authors('Lesnor', 'usa', 'ufc'))
    authors.append(Authors('nate diaz', 'usa', 'ufc'))
    authors.append(Authors('jhonson','usa','ufc'))
    authors.append(Authors('connors macgregor', 'usa', 'ufc'))
    authors.append(Authors('michael chandler', 'usa', 'ufc'))
    template_name = "djangobasicsapp/PassModel.html"
    context: dict[str, list[Authors]] = {"Authors": authors}
    return render(request, template_name, context)


