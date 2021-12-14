from django.shortcuts import redirect, render
from .models import Room
from .forms import addRoomForm
# Create your views here.
def base(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
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