from django.shortcuts import render, redirect
from app.models import Student, Chore, ChoreAssignment
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
import random
from random import shuffle
from datetime import date
import calendar

def home(request):
    chores = Chore.objects.all()
    assignments = ChoreAssignment.for_this_week()
    return render(request, 'home.html', {
        "chores": chores, 
        "monday_shuffle": assignments['monday'],
        "tuesday_shuffle": assignments['tuesday'],
        "wednesday_shuffle": assignments['wednesday'],
        "thursday_shuffle": assignments['thursday'],
        "friday_shuffle": assignments['friday']
    })

def chore_details(request):
    chores = Chore.objects.all()
    return render(request, 'chore_details.html', {"chores": chores})
def swap_chores(request):
    assignments = ChoreAssignment.for_this_week()
    if date.today().weekday() == 0:
        return render(request, 'todays_chore.html', {
            "chore": assignments['monday']
        })
    if date.today().weekday() == 1:
        return render(request, 'todays_chore.html', {
            "chore": assignments['tuesday']
        })
    if date.today().weekday() == 2:
        return render(request, 'todays_chore.html', {
            "chore": assignments['wednesday']
        })
    if date.today().weekday() == 3:
        return render(request, 'todays_chore.html', {
            "chore": assignments['thursday']
        })
    if date.today().weekday() == 4:
        return render(request, 'todays_chore.html', {
            "chore": assignments['friday']
        })
    

def todays_chore(request):
    assignments = ChoreAssignment.for_this_week()
    if date.today().weekday() == 0:
        return render(request, 'todays_chore.html', {
            "chore": assignments['monday']
        })
    if date.today().weekday() == 1:
        return render(request, 'todays_chore.html', {
            "chore": assignments['tuesday']
        })
    if date.today().weekday() == 2:
        return render(request, 'todays_chore.html', {
            "chore": assignments['wednesday']
        })
    if date.today().weekday() == 3:
        return render(request, 'todays_chore.html', {
            "chore": assignments['thursday']
        })
    if date.today().weekday() == 4:
        return render(request, 'todays_chore.html', {
            "chore": assignments['friday']
        })
    

        
class ChoreUpdate(UpdateView):
    model = Chore
    fields = ["complete"]
    template_name = "todays_chore.html"
    login_url = ''
    success_url = reverse_lazy("home")

    def test_func(self):
        return Chore.objects.get(id=self.kwargs["pk"])
    
