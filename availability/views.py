from django.shortcuts import render
from collections import defaultdict
import requests
from datetime import datetime
from .models import district_mapping

# We need only these parameters to be displayed, so we wrote a function for them to be extracted.
def batch_info(center, session):
    return {"name": [center["name"], center["address"], center["pincode"]],
            "date": session["date"],
            "age_limit": session["min_age_limit"],
            "capacity": session["available_capacity"],
            "vaccine": session["vaccine"],
            }

# We yield the values and call the above function for extraction. Yield because we will have multiple batches. ie
# values with multiple center, sessions as the vaccine will not just be available at one place
def get_batch(data):
    for center in data["centers"]:
        for session in center["sessions"]:
            yield batch_info(center, session)

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def index(request):
    # batch_list = {} Safeguard for return render() when below if is not satisfied. Update: Changed logic added else
    if 'district_id' in request.GET:
        district_id = request.GET['district_id']
        URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
        param = {'district_id': district_id, 'date': datetime.today().strftime("%d-%m-%Y")}
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
        resp = requests.get(URL, params=param, headers=header)
        data = resp.json()
        batch_list = [batch for batch in get_batch(data)]
        return render(request, 'availability/index.html', {'batch_list': batch_list})
    else:
        dmaps = district_mapping.objects.all()
        state_dist_list = [[b.state_name, b.district_name] for b in dmaps]
        d1 = defaultdict(list)
        for k, v in state_dist_list:
            d1[k].append(v)
        state_dist_dict = dict((k, tuple(v)) for k, v in d1.items())
        dist_id_dict = {c.district_name: c.district_id for c in dmaps}
        return render(request, 'availability/index.html', {'dist_id_dict': dist_id_dict, 'state_dist_dict': state_dist_dict})