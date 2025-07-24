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
        {
            'user': 'Prince Kumar',
            'position': 'Junior Front-End Developer',
            'profile': 'prince.jpg',
            'content': '''🚨 !!hashtag#Hiring Hiring Hiring !! 🚨 😎🚀 Position - Junior Front-End Developer 
             Location - (Remote)
             Experience:- Intern To 5 Year
             Stipend: $600 - $4200 per month
             Day Shift - 11: 00am- 5: 00pm
             Qualification - Graduation/Freshers''',
            'image': 'higheri.gif',
            'likes': 300,
            'comments': 15,
            'shares': 4,
        },
        {
            'user': 'Prachi Saxena',
            'position': '| DSA | Frontend Developer',
            'profile': 'prachi.jpeg',
            'content': 'Thrilled to share that I have successfully completed the Deloitte Technology Job Simulation and earned a certification! 😎🚀',
            'image': 'prschipost.jpeg',
            'likes': 300,
            'comments': 55,
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
        {
            'user': 'kundan kumar',
            'position': 'Full Stack Developer',
            'profile': 'kundan.jpeg',
            'content': '''🚀 Excel Dashboard Project: Sales Analysis for FNP (Ferns N Petals) 🎁📈

            Just wrapped up an end-to-end Sales Analysis project for FNP – one of India's leading online gifting platforms, using Microsoft Excel only! 🧑‍💻✨''',
            'image': 'kp.jpeg',
            'likes': 20,
            'comments': 2,
            'shares': 1,
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