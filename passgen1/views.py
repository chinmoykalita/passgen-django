from django.http import HttpResponse
from django.shortcuts import render
from .models import Userpass
import requests
import json

def index(request):
    return render(request, 'passgen1/index.html')

def result(request):
    password = request.POST.get('password', 'default')

    #saving user input to database
    if request.method=='POST':
        passw = Userpass(user_password=password)
        passw.save()
    else:
        pass    

    #main function(algorithm for processing passwords)
    SECURE = (('a','@'), ('o', '0'), ('i','1'), ('H', '#'), ('h', '#'), ('A', '@'),('S', '$'), ('H', '#'), ('O', '0'), ('I', '!'), ('And', 'nd'), ('123', '231'))
    
    
    def securePassword(password): 
        for a, b in SECURE:
            password = password.replace(a, b)
        return password    
    
    password = securePassword(password)
        

    params = {'rpass':password}


    #preventing user to directly go to result page
    if request.method=='POST':
        return render(request, 'passgen1/result.html', params)
    else:
        return HttpResponse("<h2>LOL Error, You can't access this page without entering the password;)</h2>")    

def recharge(request):
    API_KEY = '9wAdHsUZTbOBeQWc6Kml7N28fIXvq5jREMLkaVn1JDzx0SpCui'
    URL = 'https://api.payben.in/recharge-api/balance.php?api_key=9wAdHsUZTbOBeQWc6Kml7N28fIXvq5jREMLkaVn1JDzx0SpCui'
    # params={'key': '9wAdHsUZTbOBeQWc6Kml7N28fIXvq5jREMLkaVn1JDzx0SpCui'}
    response = requests.get(URL,  headers={"User-Agent": "XY"})
    print(response)
    response = response.json()

    print(response)
    return HttpResponse(str(response))