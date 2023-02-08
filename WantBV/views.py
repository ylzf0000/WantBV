import os
import base64
import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

from WantBV.settings import STATICFILES_DIRS

STATICFILES_DICT = {x[0]: x[1] for x in STATICFILES_DIRS}


def image(request):
    ctx = {

        # "image_dirs":image_dirs
    }
    # print(ctx)
    return render(request, 'image.html', ctx)


def get_image_dirs(request):
    print("request:", request)
    # if request.GET:
    images_dir = STATICFILES_DICT["images"]
    dbtype_list = os.listdir(images_dir)
    image_dirs = [{'full_dir': os.path.join(images_dir, f), 'dir': f}
                  for f in dbtype_list if os.path.isdir(os.path.join(images_dir, f))]
    print(image_dirs)
    ret = {'image_dirs': image_dirs}
    ret = JsonResponse(ret)
    return ret

# def get_img(request):
#     imagepath = "photo/123.png"
#     # image_data =imagepath
#     return HttpResponse(image_data, content_type="image/png")

#
# def overall(request):
#     ctx = {}
#     ctx['num_diabetes_complication'] = data_process.barData()
#     ctx['scatterData'] = data_process.scatterData()
#     ctx['bloodPressureData'] = data_process.bloodPressureData()
#     ctx['diseaseRelationshipData'] = data_process.relationshipData()
#     ctx['biochemicalIndexesData'] = data_process.biochemicalIndexesData()
#     return render(request, 'overall.html', ctx)
#
#

#
#
# def getPatientInfo(request):
#     if request.POST:
#         id = request.POST['id']
#         ret = data_process.getPatientInfo(id)
#         ret = {'data': ret}
#         ret = JsonResponse(ret)
#         return ret
#
#
# def getAbnormalAttr(request):
#     if request.POST:
#         id = request.POST['id']
#         ret = data_process.getAbnormalAttr(id)
#         ret = {'data': ret}
#         ret = JsonResponse(ret)
#         return ret
#
# def getRadarInfo(request):
#     if request.POST:
#         id = request.POST['id']
#         ret = data_process.getRadarData(id)
#         ret = {'data': ret}
#         ret = JsonResponse(ret)
#         return return
