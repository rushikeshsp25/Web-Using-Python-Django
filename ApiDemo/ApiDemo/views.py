from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

data = {
    'name':'rushi',
    'role':'Software Developer'
}

@require_http_methods(["GET"])
def getData(request):
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["POST"])
def postData(request):
    #request.POST is a QueryDict we need to conver it to python dict using .dict()
    print(request.POST.dict())
    data.update(request.POST.dict())    #update is a dictionary method to update a dictionary from another dictionary
    print(request.POST.get('username')) 
    return JsonResponse(data)
