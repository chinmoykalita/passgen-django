from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    password = request.POST.get('password', 'default')
    print(password)

    SECURE = (('a','@'), ('o', '0'), ('i','1'), ('H', '#'), ('h', '#'), ('A', '@'),('S', '$'), ('H', '#'), ('O', '0'), ('I', '!'), ('And', 'nd'), ('123', '231'), ('12345', '52314'),("password", "TuPaagalHe@"), ('Password', 'TuPaagalHe@00'), ('Fardin', 'Dinfar'), ('s', '$'), ('and', '&'), )
    
    
    def securePassword(password): 
        for a, b in SECURE:
            password = password.replace(a, b)
        return password    
    
    password = securePassword(password)
        

    params = {'rpass':password}
            
    return render(request, 'result.html', params)

