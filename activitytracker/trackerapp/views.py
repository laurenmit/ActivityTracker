from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity, Totals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import ActivityForm
from datetime import timedelta


#------- Auxiliary functions for views ----------
def get_totals():
    if not(Totals.objects.filter(user="wizard").exists()):
        totals = Totals(user="wizard")
        totals.save()
    totals = Totals.objects.all().get(user="wizard")
    return totals

def average_pace(distance_km, time_total):
    if time_total > 0:
        avg_pace = float(distance_km)/(time_total/3600)
    else:
        avg_pace = 0
    return round(avg_pace,2)

#adapted from https://stackoverflow.com/questions/2780897/python-summing-up-time
def get_seconds(time1):
    total_secs = 0
    time1 = str(time1)
    time1_split = [int(s) for s in time1.split(':')]
    total_secs+= ((time1_split[0] * 60 + \
    time1_split[1]) * 60 + (time1_split[2]))
    return total_secs

def format_time_string(total_secs):
    total_secs, sec = divmod(total_secs, 60)
    hr, min = divmod(total_secs, 60)
    time_total = "%02d:%02d:%02d" % (hr, min, sec)
    return time_total


#Home page with form to capture activity DjangoTemplates
class HomeView(TemplateView):
    template_name="trackerapp/home.html"

    def get(self, request):
        form = ActivityForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.cleaned_data
            action = Activity(distance_km=activity['distance_km'],
                            time_stamp =activity['time_stamp'],
                            activity_type = activity['activity_type'],
                            date = activity['date'])
            action.save()

            totals = get_totals()
            add_time = get_seconds(action.time_stamp)
            totals.distance_km =  totals.distance_km + action.distance_km
            totals.time_total += add_time

            if action.activity_type == 'walk':
                totals.walk_time += add_time

            elif action.activity_type == 'run':
                totals.run_time += add_time

            elif action.activity_type == 'hike':
                totals.hike_time += add_time

            elif action.activity_type == 'cycle':
                totals.bike_time += add_time

            elif action.activity_type == 'swim':
                totals.swim_time += add_time

            else:
                totals.other_time += add_time
            totals.save()
            form = ActivityForm()
            return render(request, self.template_name, {'form':form})
        else:
            return render(request, self.template_name, {'form':form})

#Results page to show progress, no form
class ResultsView(TemplateView):
    template_name="trackerapp/results.html"

    def get(self, request):
        totals = get_totals()
        time_stamp = format_time_string(totals.time_total)
        avg_pace = average_pace(totals.distance_km, totals.time_total)
        progress = totals.distance_km/520 * 100
        progress = round(progress,2)
        if progress >= 100:
            success = 1
        else:
            success = 0
        return render(request, self.template_name, {'totals':totals,
                                                    'time_stamp':time_stamp,
                                                    'avg_pace':avg_pace,
                                                    'progress':progress,
                                                    'success':success})
