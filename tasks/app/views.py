from django.shortcuts import render,redirect
from django.core.mail import send_mass_mail,BadHeaderError
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Feedback
from django.http import HttpResponse
from .forms import FeedbackForm
# Create your views here.
@login_required(login_url='/login')
def feedback(request):
    if request.method=='POST':
     form=FeedbackForm(request.POST)
     if form.is_valid():
        subject=request.POST['subject']
        rating=request.POST['rating']
        email=request.POST['email']
        comments=request.POST['comments']
        k=form.save(commit=False)
        k.user = request.user
        k.save()
        try:
            m1=(f"Feedback Form By {k.user}",f"Subject:{subject} \n Rating:{rating} \n Feedback:{comments} ", email, [settings.EMAIL_HOST_USER,email])
            m2=("Thank for your response","please keep giving regular feedback",settings.EMAIL_HOST_USER,[email])
            send_mass_mail((m1, m2), fail_silently=False)
        except BadHeaderError:
            return HttpResponse("Invalid header found.")

        return redirect('/feed')
    form=FeedbackForm()
    return render(request,'app/feedback.html',{"form":form})
class FeedListView(LoginRequiredMixin,ListView):
    model=Feedback
    context_object_name='feed'
    def get_queryset(self):
        return Feedback.objects.filter(user=self.request.user).order_by('-id')
    
@login_required(login_url='/login')
def display(request):
    return render(request,'app/display.html')
