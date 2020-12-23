from django.shortcuts import render
from .models import Job
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER
from .forms import ContactModelForm


# Create your views here.
def home(request):
    jobs = Job.objects
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', context)


def about(request):
    return render(request, 'jobs/about.html', {})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']

        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()

        send_mail(
            'Comments from ' + name + ' for ForeverMyWanderlust',
            comments,
            EMAIL_HOST_USER,
            ['anamitradey.ece@gmail.com', 'sagarikapaul6@gmail.com', email]
        )

        context = {
            'name': name
        }

        return render(request, 'jobs/contact.html', context)
    else:
        return render(request, 'jobs/contact.html', {})
