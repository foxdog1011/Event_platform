from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventRegistration
from .forms import EventForm, CommentForm
from rest_framework import viewsets
from .serializers import EventSerializer

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_create(request):
    user_profile = request.user.event_profile  
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'user_profile': user_profile})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk, author=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, author=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def event_register(request, pk):
    event = get_object_or_404(Event, pk=pk)
    registration, created = EventRegistration.objects.get_or_create(event=event, participant=request.user)
    if created:
        messages.success(request, '報名成功！')
    else:
        messages.info(request, '您已報名该事件。')
    return redirect('event_detail', pk=event.pk)

def event_registrations(request, pk):
    event = get_object_or_404(Event, pk=pk, author=request.user)
    registrations = EventRegistration.objects.filter(event=event)
    return render(request, 'events/event_registrations.html', {'event': event, 'registrations': registrations})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    comments = event.comments.all()
    user_profile = request.user.event_profile  

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.author = request.user
            comment.save()
            return redirect('event_detail', pk=event.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'events/event_detail.html', {
        'event': event,
        'comments': comments,
        'comment_form': comment_form,
        'user_profile': user_profile
    })

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
