from django.shortcuts import render, get_object_or_404, redirect
from .models import Workout
from .forms import WorkoutForm

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'fitness/workout_list.html', {'workouts': workouts})

def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'fitness/workout_detail.html', {'workout': workout})

def workout_create(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm()
    return render(request, 'fitness/workout_form.html', {'form': form})

def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'fitness/workout_form.html', {'form': form})

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        workout.delete()
        return redirect('workout_list')
    return render(request, 'fitness/workout_confirm_delete.html', {'workout': workout})

