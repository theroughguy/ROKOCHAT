from django.shortcuts import render,HttpResponse
from agora_token_builder import RtcTokenBuilder
import random
from . models import RoomMember
import time
# Create your views here.
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
def getToken(request):


    appId = '40858ac22a8b45ff85299046c0ba59d2'
    appCertificate = '90785d84bc6d448ea3b4a1e0fb9cdb7b'


    channelName = request.GET.get('channel')

    uid = random.randint(1,232)

    role = 1

    timestamp = time.time()

    expirationtime = 3600*24
    privilegeExpiredTs = timestamp + expirationtime




    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token':token , 'uid':uid},safe=False)


def home(request):


    return render(request,template_name='videochat/home.html')





def room(request):



    return render(request,template_name='videochat/room.html')





@csrf_exempt
def createmember(request):

    data = json.loads(request.body)

    member,created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']

    )


    return JsonResponse({'name':data['name']},safe=False)




def getmember(request):




    uid = request.GET.get('UID')

    room_name = request.GET.get('room_name')



    member = RoomMember.objects.get(

        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name},safe=False)



@csrf_exempt
def deletemember(request):

    data = json.loads(request.body)

    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']

    )

    member.delete()

    return JsonResponse('member Was deleted',safe=False)