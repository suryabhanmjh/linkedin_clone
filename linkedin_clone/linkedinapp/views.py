from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    posts = [
        {
            'user': 'Suman Kumar',
            'position': 'Software Intern',
            'profile': 'suman.jpg',
            'content': '🎉 Thrilled to share that I have completed the Deloitte Technology Job Simulation on Forage!',
            'image': 'certificate.png',
            'likes': 3864,
            'comments': 227,
            'shares': 5,
        },
        {
            'user': 'Anshi Gupta',
            'position': 'Backend Developer',
            'profile': 'anchal.jpg',
            'content': 'Skipped parties. Missed many trips. Said no to outings 🥳',
            'image': 'anchal_mantra.jpg',
            'likes': 1200,
            'comments': 140,
            'shares': 4,
        },
        {
            'user': 'Suryabhan Singh',
            'position': 'Full Stack Developer',
            'profile': 'profile.jpg',
            'content': 'Just completed my LinkedIn clone using Django! 😎🚀',
            'image': 'linkedin-post.png',
            'likes': 900,
            'comments': 75,
            'shares': 2,
        },
    ]
    return render(request, 'linkedinapp/home.html', {'posts': posts})


def profile(request):
    return render(request, 'linkedinapp/profile.html')

def jobs(request):
    return render(request, 'linkedinapp/jobs.html')
def messaging(request):
    return render(request, 'linkedinapp/messaging.html')
def notifications(request):
    return render(request, 'linkedinapp/notifications.html')
def settings(request):
    return render(request, 'linkedinapp/settings.html')
def mynetwork(request):
    return render(request, 'linkedinapp/mynetwork.html')