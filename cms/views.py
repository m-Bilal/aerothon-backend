from django.core import serializers
from django.http import HttpResponse, JsonResponse


from django.views.decorators.csrf import csrf_exempt

from cms import models

# Create your views here.

def hello(request):
    return HttpResponse("Hello world")


@csrf_exempt
def get_feed(request):
    all_feed = models.Headline.objects.all()
    json = serializers.serialize('json', all_feed)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_feed_for_id(request):
    id = request.POST.get('id', '')
    feed = models.Headline.objects.filter(id=id)
    json = serializers.serialize('json', feed)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_aircraft_model_for_id(request):
    id = request.POST.get('id', '')
    model = models.AircraftModel.objects.filter(id=id)
    json = serializers.serialize('json', model)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_aircraft_for_id(request):
    id = request.POST.get('id', '')
    model = models.Aircraft.objects.filter(id=id)
    json = serializers.serialize('json', model)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_airport_for_id(request):
    id = request.POST.get('id', '')
    model = models.Airport.objects.filter(id=id)
    json = serializers.serialize('json', model)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_flight_for_id(request):
    id = request.POST.get('id', '')
    model = models.Flight.objects.filter(id=id)
    json = serializers.serialize('json', model)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_aircraft_models(request):
    all_models = models.Aircraft.objects.all()
    json = serializers.serialize('json', all_models)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_aircraft_for_msn(request):
    msn = request.POST.get('msn', '')
    model = models.Aircraft.objects.filter(msn=msn)
    json = serializers.serialize('json', model)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_all_flights_for_msn(request):
    msn = request.POST.get('msn', '')
    model = models.Flight.objects.filter(aircraft__msn=msn)
    json = serializers.serialize('json', model)
    return JsonResponse(json, safe=False)


@csrf_exempt
def get_all_flights_for_msn_filter(request):
    ''''''


@csrf_exempt
def get_flight_info(request):
    flight_no = request.POST.get('flight_no', '')
    model = models.Flight.objects.filter(flight_no=flight_no)
    json = serializers.serialize('json', model)
    return JsonResponse(json, safe=False)

