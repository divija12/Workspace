'''
Class CalendarView used to view calendar of today's date, month, year
def get_context_data(..):
    overrides existing function to calculate prev_month, next_month and form the calendar
    for navigating the calendar

Function to add and edit Events to calendar
def event(..):
    if event_id exists:
        View, edit existing event
    else:
        Let user create a new event
'''

from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar
from .forms import EventForm

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendarapp/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use today's date for generating the calendar
        d = self.get_date(self.request.GET.get('month', None))
        # Instantiate calendar class with today's year and date
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = Calendar.prev_month(cal, d)
        context['next_month'] = Calendar.next_month(cal, d)
        return context

    def get_date(self, req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return datetime.today()

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    return render(request, 'calendarapp/event.html', {'form': form})