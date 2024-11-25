from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sample(request):
    return HttpResponse("this file is just a sample file")

def sample2(resuest):
    return HttpResponse("<h1>this file is second a sample file</h1>")

def sample3(request):
    return HttpResponse("<h1> <marquee>Shreyosi Paul<marque></h1>")



def sample4(request):
    return HttpResponse('''
        <h1><marquee> Name is Shreyosi</marque> </h1>
        <h3><i> Age is 23 </i><h3>
        <h2><b> Home is Kolkata </b><h2>
        <img src="https://w0.peakpx.com/wallpaper/377/534/HD-wallpaper-tom-and-jerry-cartoon-pink-background-animated.jpg" alt="Tom and Jerry" width="200" height="300">
        
        
    ''')
    
def sample5(request):
    return HttpResponse('''<img src="https://w0.peakpx.com/wallpaper/377/534/HD-wallpaper-tom-and-jerry-cartoon-pink-background-animated.jpg" alt="Tom and Jerry" width="200" height="300">''')

