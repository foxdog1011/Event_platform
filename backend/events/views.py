from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm
from django.contrib import messages
from .models import Event, EventRegistration
from .forms import CommentForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

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
    registration, created = EventRegistration.objects.get_or_create(event=event, attendee=request.user)
    if created:
        messages.success(request, '报名成功！')
    else:
        messages.info(request, '您已报名该事件。')
    return redirect('event_detail', pk=event.pk)

def event_registrations(request, pk):
    event = get_object_or_404(Event, pk=pk, author=request.user)
    registrations = EventRegistration.objects.filter(event=event)
    return render(request, 'events/event_registrations.html', {'event': event, 'registrations': registrations})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    comments = event.comments.all()
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
    return render(request, 'events/event_detail.html', {'event': event, 'comments': comments, 'comment_form': comment_form})
