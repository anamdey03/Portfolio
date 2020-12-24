from django.shortcuts import render
from .models import Job
from django.core.mail import send_mail, EmailMessage
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
        phone = request.POST['phone']
        comments = request.POST['comments']

        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()

        email = EmailMessage(
            'Comments from ' + name + ' for ForeverMyWanderlust',
            comments + '\n\nThanks & Regards, \n' + name + '\n' + phone,
            EMAIL_HOST_USER,
            ['sagarikapaul6@gmail.com'],
            cc=[email],
            bcc=['anamitradey.ece@gmail.com'],
            reply_to=[email],
        )

        email.send(fail_silently=True)

        context = {
            'name': name
        }

        return render(request, 'jobs/contact.html', context)
    else:
        return render(request, 'jobs/contact.html', {})
