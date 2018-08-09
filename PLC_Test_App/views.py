from django.shortcuts import render
from django.shortcuts import HttpResponse
import json


def index(request):
    return render(request, 'index.html')


def get_data(request):
    with open('testdata_2.json') as f:
        data = json.load(f)
    return HttpResponse(json.dumps(data), content_type="application/json")


def set_data(request):
    switch_num = request.POST.get('switch', '')
    switch_state = request.POST.get('state', '')
    with open('testdata.json', 'r+') as f:
        data = json.load(f)
        data['input_' + switch_num] = int(switch_state)
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()
    return HttpResponse()


def run_test(request):
    plc_outputs = [{"output_0": 0,
                    "output_1": 0,
                    "output_2": 0,
                    "output_3": 0},
                   {"output_0": 0,
                    "output_1": 1,
                    "output_2": 1,
                    "output_3": 0},
                   {"output_0": 0,
                    "output_1": 0,
                    "output_2": 1,
                    "output_3": 1},
                   {"output_0": 1,
                    "output_1": 0,
                    "output_2": 1,
                    "output_3": 0},
                   {"output_0": 1,
                    "output_1": 1,
                    "output_2": 1,
                    "output_3": 0}]
    with open('testdata_3.json') as f:
        data = json.load(f)
    for test_run in data:
        print(test_run)
