from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Room, Topic
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import addRoomForm
# Create your views here.
def signin(request):
    page='signin'
    if request.user.is_authenticated:
        return redirect('base')
    
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnot exist')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            messages.error(request, 'User username or password doesnot match')


    context = {"page":page}
    return render(request, 'root/login_registration.html',context )

def signout(request):
    logout(request)
    return redirect('base')
def signup(request):
    form=UserCreationForm()
    if request.method== 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('base')
        else:
            messages.error(request,"An error occured")

    context={"form":form}
    return render(request, "root/login_registration.html",context)

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
@login_required(login_url='signin')
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