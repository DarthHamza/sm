from django.shortcuts import render, redirect

def profile(request):
    if request.user.is_anonymous:
        return redirect('signin')

    return render(request, 'profile.html')
