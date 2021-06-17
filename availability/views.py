from django.shortcuts import render
from django.http import HttpResponse
import simplejson
from availabilityupdater.availability_updater import *

def index(request):
    if 'selecteddistrict' in request.GET:
        selecteddistrict = request.GET['selecteddistrict']
        batch_list = fetch_data(selecteddistrict)
        return render(request, 'availability/index.html', {'batch_list': batch_list})
    else:
        state_dist_dict = state_dist()
        return render(request, 'availability/index.html', {'state_dist_dict': state_dist_dict})


def getdistrict(request):
    state_name = request.GET['state']
    state_dist_dict = state_dist()
    district_list = [district for district in state_dist_dict[state_name]]
    return HttpResponse(simplejson.dumps(district_list), content_type='application/json')


def scheduledata(request):
    district_name = request.GET['district']
    batch_list = fetch_data(district_name)
    message_list = []
    for batch in batch_list:
        if batch["capacity"] > 0:
            message = "Vaccine available at {} {} {}.<br/> Minimum Age: {}.<br/> Capacity: {}.<br/>" \
                      "Vaccine: {}".format(batch["name"][0], batch["name"][1], batch["name"][2], batch["age_limit"],
                                               batch["capacity"], batch["vaccine"])
            message_list.append(message)
    if not message_list:
        message = "No vaccine available currently"
        return HttpResponse(simplejson.dumps(message), content_type='application/json')
    return HttpResponse(simplejson.dumps(message_list), content_type='application/json')
