from django.shortcuts import render , redirect 
from .models import Room  , Message
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    username = request.user.username
    return render(request , "home.html" , {"username":username})

@login_required
def room(request , room):
    room_details = Room.objects.get(name=room)
    username = request.user.username
    return render(request , "room.html" , {"username":username , "room_details":room_details , "room":room})

def checkview(request):
    room = request.POST["room_name"]
    username = request.user.username
    
    if Room.objects.filter(name=room).exists():
        return redirect("/chat/"+room+"/?username="+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect("/chat/"+room+"/?username="+username)
    
def send(request):
    username = request.user.username
    
    message = request.POST["message"]
    room_id = request.POST["room_id"]
    
    new_message = Message.objects.create(value=message , user=username , room=room_id)
    new_message.save()
    return HttpResponse("Message sent successfully")
    
def getMessages(request , room):
    room_details = Room.objects.get(name=room)
    
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values("value", "user", "date"))})  # Güncellendi: values() metoduna alan isimleri eklendi
