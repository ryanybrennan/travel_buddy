from django.shortcuts import render, HttpResponse, redirect
from ..login_reg.models import User
from .models import Travel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
# Create your views here.
def index(request):
    return redirect('/main')
def login_reg(request):
    return render(request, 'travel_bud/login_reg.html' )
def home(request):
    context={
    'travels':Travel.objects.filter(user__username = request.session['user']),
    'joiners':Travel.objects.filter(people__username = request.session['user']),
    'others': Travel.objects.exclude(user__username= request.session['user']).exclude(people__username = request.session['user']),
    }
    print Travel.objects.filter(user__username =request.session['user'])
    print Travel.objects.exclude(people__username= request.session['user'])
    print Travel.objects.exclude(user__username = request.session['user'])
    return render(request, 'travel_bud/home.html', context)
def add(request):
    return render(request, 'travel_bud/add_travel.html')
def destination(request, id):
    context={
    'travels': Travel.objects.get(id=id),
    }
    return render(request, 'travel_bud/destination.html', context)
def create(request):
    trip = Travel.TravelManager.trip(request.POST)
    planner = User.objects.get(username = request.session['user'])
    if trip[0]== False:
        x =Travel.objects.create(destination = request.POST['destination'], description = request.POST['description'], travel_from = request.POST['travel_from'], travel_to=request.POST['travel_to'], user = planner)
        # x.people.add(User.objects.get(username=request.session['user']))
        x.save()
        return redirect('travel_dash')
    else:
        errors = trip[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
        return redirect('add_trip')
def join(request, id):
    trip = Travel.objects.get(id=id)
    trip.people.add(User.objects.get(username=request.session['user']))
    trip.save()
    return redirect('travel_dash')
