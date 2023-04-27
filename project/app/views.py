from django.shortcuts import render
from app.models import Ticket
from django.shortcuts import redirect 
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def main(request):
	return render(request,"index.html")
def taj(request):
	return render(request,"monument_info/taj.html")
def aja(request):
	return render(request,"monument_info/aja.html")
def elo(request):
	return render(request,"monument_info/elo.html")
def jan(request):
	return render(request,"monument_info/jan.html")
def khaj(request):
	return render(request,"monument_info/khaj.html")
def qua(request):
	return render(request,"monument_info/qua.html")
def red(request):
	return render(request,"monument_info/red.html")
def sar(request):
	return render(request,"monument_info/sar.html")
def sun(request):
	return render(request,"monument_info/sun.html")
def gogo(request):
	if request.method=="POST":
		fname=request.POST.get("fn")
		lname=request.POST.get("ln")
		email=request.POST.get("em")
		phone=request.POST.get("ph")
		dat=request.POST.get("da")
		id_no=request.POST.get("no")
		ticket=Ticket(fname=fname,lname=lname,email=email,phone=phone,dat=dat,id_no=id_no)
		ticket.save()
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
def dbms(request):
	mydata = Ticket.objects.all().values()
	template = loader.get_template('template.html')
	context = {
	  'mymembers': mydata,
	}
	return HttpResponse(template.render(context, request))