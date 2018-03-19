from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Follow

def profile(request, pk):
    if request.user.is_anonymous:
        return redirect('signin')

    context = {
        "user": User.objects.get(pk=pk)
    }
    return render(request, 'profile.html', context)

def search_users(request):
    if request.user.is_anonymous:
        return redirect('signin')

    prey_list = []
    preys = request.user.stalker.all()
    for prey in preys:
        prey_list.append(prey.prey)

    users = User.objects.none()

    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)

    context = {
        "users":users,
        "prey_list":prey_list
    }
    return render(request, 'search_users.html', context)

def follow(request, pk):
    if request.user.is_anonymous:
        return redirect('signin')

    prey = User.objects.get(pk=pk)
    stalker = request.user

    follow, created = Follow.objects.get_or_create(stalker=stalker, prey=prey)
    if created:
        messages.success(request, "Successfully followed %s!"%(prey))
    else:
        follow.delete()
        messages.success(request, "Unfollowed %s!"%(prey))

    return redirect('search-users')

def followers(request, pk):
    if request.user.is_anonymous:
        return redirect('signin')

    user = request.user
    followers = user.prey.all()
    context = {
        "followers": followers,
    }
    return render(request, 'followers.html', context)

def following(request, pk):
    if request.user.is_anonymous:
        return redirect('signin')

    user = request.user
    following = user.stalker.all()
    context = {
        "following": following,
    }
    return render(request, 'following.html', context)
