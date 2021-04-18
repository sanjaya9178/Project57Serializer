from django.shortcuts import render
from app57.models import student
from app57.serializer import studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
def studentdetails(request):
    stu=student.objects.get(id=1)
    serializer=studentserializer(stu)
    # json_data=JSONRenderer.render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

# QuerySet - All student data
def student_list(request):
    stu=student.objects.get(id=1)
    serializer=studentserializer(stu)
    json_data=JSONRenderer.render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
