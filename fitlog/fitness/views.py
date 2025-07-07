from django.shortcuts import render, redirect, get_object_or_404
from .models import WorkoutEntry
from .forms import WorkoutEntryForm

def workout_list(request):
    workouts = WorkoutEntry.objects.all().order_by('-date')
    return render(request, 'fitness/workout_list.html', {'workouts': workouts})

def workout_detail(request, pk):
    workout = get_object_or_404(WorkoutEntry, pk=pk)
    return render(request, 'fitness/workout_detail.html', {'workout': workout})

def workout_create(request):
    if request.method == 'POST':
        form = WorkoutEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutEntryForm()
    return render(request, 'fitness/workout_form.html', {'form': form})

def workout_edit(request, pk):
    workout = get_object_or_404(WorkoutEntry, pk=pk)
    if request.method == 'POST':
        form = WorkoutEntryForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', pk=pk)
    else:
        form = WorkoutEntryForm(instance=workout)
    return render(request, 'fitness/workout_form.html', {'form': form})

def workout_delete(request, pk):
    workout = get_object_or_404(WorkoutEntry, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'fitness/workout_confirm_delete.html', {'workout': workout})

