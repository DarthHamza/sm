from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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

    users = User.objects.none()

    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)

    context = {
        "users":users,
    }
    return render(request, 'search_users.html', context)
