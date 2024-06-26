from django.shortcuts import render
from app.models import Ticket
from django.shortcuts import redirect 
from django.http import HttpResponse
from django.template import loader
import requests

def get_weather(city):
    complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dfa9faccacf43fd910a9c1a7a9cd3f72"
    response = requests.get(complete_url)
    return response.json()

def main(request):
	return render(request,"index.html")
def taj(request):
	context = {
        'weather': get_weather('Agra')
    }
	return render(request,"monument_info/taj.html", context)
def aja(request):
	context = {
        'weather': get_weather('Aurangabad')
    }
	return render(request,"monument_info/aja.html", context)
def elo(request):
	context = {
        'weather': get_weather('Aurangabad')
    }
	return render(request,"monument_info/elo.html", context)
def jan(request):
	context = {
        'weather': get_weather('Delhi')
    }
	return render(request,"monument_info/jan.html", context)
def khaj(request):
	context = {
        'weather': get_weather('Chhatarpur')
    }
	return render(request,"monument_info/khaj.html", context)
def qua(request):
	context = {
        'weather': get_weather('Delhi')
    }
	return render(request,"monument_info/qua.html", context)
def red(request):
	context = {
        'weather': get_weather('New Delhi')
    }
	return render(request,"monument_info/red.html", context)
def sar(request):
	context = {
        'weather': get_weather('Kevadia')
    }
	return render(request,"monument_info/sar.html", context)
def sun(request):
	context = {
        'weather': get_weather('Konarak')
    }
	return render(request,"monument_info/sun.html", context)
def gogo(request):
	#print('ticket generated')
	if request.method=="POST":
		fname=request.POST.get("firstname")
		lname=request.POST.get("lastname")
		email=request.POST.get("email")
		phone=request.POST.get("phone")
		dat=request.POST.get("startDate")
		id_no=request.POST.get("no")

		gender=request.POST.get("gender")
		nationality=request.POST.get("nationality")
		print(fname,lname,email, phone,dat,id_no,gender,nationality)
		ticket=Ticket(fname=fname,lname=lname,email=email,phone=phone,dat=dat,id_no=id_no)
		ticket.save()
		print('DOne')
		return redirect("/")
	return render(request,"index.html")

def tajbook(request):
	context={
	'monuname':'Taj Mahal',
	'price':'120'
	}
	return render(request,"new_ticket/index.html",context)
def ajabook(request):
	context={
	'monuname':'Ajanta Caves',
	'price':'25'
	}
	return render(request,"new_ticket/index.html",context)
def elobook(request):
	context={
	'monuname':'Ellora Caves',
	'price':'30'
	}
	return render(request,"new_ticket/index.html",context)
def janbook(request):
	context={
	'monuname':'Jantar Mantar ',
	'price':'20'
	}
	return render(request,"new_ticket/index.html",context)
def khajbook(request):
	context={
	'monuname':'Khajuraho',
	'price':'30'
	}
	return render(request,"new_ticket/index.html",context)
def quabook(request):
	context={
	'monuname':'Qutub Minar ',
	'price':'25'
	}
	return render(request,"new_ticket/index.html",context)
def redbook(request):
	context={
	'monuname':'Red Fort',
	'price':'25'
	}
	return render(request,"new_ticket/index.html",context)
def sarbook(request):
	context={
	'monuname':'Statue of Unity',
	'price':'35'
	}
	return render(request,"new_ticket/index.html",context)
def sunbook(request):
	context={
	'monuname':'Sun Temple',
	'price':'30'
	}
	return render(request,"new_ticket/index.html",context)
# def dbms(request):
# 	mydata = Ticket.objects.all().values()
# 	template = loader.get_template('template.html')
# 	context = {
# 	  'mymembers': mydata,
# 	}
# 	return HttpResponse(template.render(context, request))


st="""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Admin Panel</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body class="m-5">
    <center><h3 class="text-primary">Bookings List</h3></center>
    <div class="container">
        <div class="row">
            <div class="col">
                <table class="table">
                    <tbody><!--Ye Heading hai isko rahne dena-->
                        <tr class="text-uppercase" >
                            <td style='background-color:#fedbc5' class="text-dark border border-dark p-2">ID</td>
                            <td style='background-color:#fedbc5' class="text-dark border border-dark p-2">fName</td>
                            <td style='background-color:#fedbc5' class="text-dark border border-dark p-2">lName</td>
                            <td style='background-color:#fedbc5' class="text-dark border border-dark p-2">Email</td>
                            <td style='background-color:#fedbc5' class="text-dark border border-dark p-2">Phone</td>
                            <td style='background-color:#fedbc5' class="text-dark border border-dark p-2">Date</td>
                            <td style='background-color:#fedbc5' class="text-dark border border-dark p-2">ID No.</td>
                        </tr>"""
ed="""</tbody></table></div></div></div>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
</html>"""

rst="""<td class="text-primary bg-info bg-opacity-10 border border-danger rounded-end p-2">"""
tend='</td>'

def dbms(request):
	tickets = Ticket.objects.all()
	output = ''
	for ticket in tickets:
		output += f"<tr>{rst}{ticket.id}{tend}{rst}{ticket.fname}{tend}{rst}{ticket.lname}{tend}{rst}{ticket.email}{tend}{rst}{ticket.phone}{tend}{rst}{ticket.dat }{tend}{rst}{ticket.id_no}{tend}</tr>"
	return HttpResponse(st+output+ed)