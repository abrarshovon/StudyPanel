from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Room, Topic
from .forms import addRoomForm
# Create your views here.
def base(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    rooms=Room.objects.filter(Q(topic__name__icontains=q) | Q(title__icontains=q) )
    totalroom=rooms.count()
    topics=Topic.objects.all()
    context={'rooms':rooms,'topics':topics, 'totalroom':totalroom}
    return render(request, 'root/main.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room' : room}
    return render(request, 'root/room.html',context)

def addRoom(request):
    form = addRoomForm()
    if request.method == 'POST':
        form=addRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    context={'form':form}
    return render(request, 'root/room_up_create.html',context)

def updateRoom(request,pk):
    room= Room.objects.get(id=pk)
    form= addRoomForm(instance=room)
    if request.method == 'POST':
        form=addRoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('base')
    context ={'form':form}
    return render(request, 'root/room_up_create.html', context)

def deleteRoom(request,pk):
    room= Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base')
    return render(request, 'root/delete.html',{'item':room} )