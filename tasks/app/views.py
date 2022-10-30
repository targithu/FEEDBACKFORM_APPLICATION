from django.shortcuts import render,redirect
from django.core.mail import send_mass_mail,BadHeaderError
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Feedback
from django.http import HttpResponse
from .forms import FeedbackForm
# Create your views here.
#superuser:taruser
#password:1@2@3
#username:taru
#password:321321321@
#username:tsh
#password:@321321321
@login_required(login_url='/login')
def feedback(request):
    if request.method=='POST':
     form=FeedbackForm(request.POST)
     if form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        Comments=form.cleaned_data['Comments']
        t=form.save(commit=False)
        try:
            m1=(name, Comments, email, ["trialpyexpt@gmail.com"])
            m2=("Thank for your response",f"Your Response :{Comments}",email,[email])
            send_mass_mail((m1, m2), fail_silently=False)
        except BadHeaderError:
            return HttpResponse("Invalid header found.")

        return redirect('/feed')
    form=FeedbackForm()
    return render(request,'app/feedback.html',{"form":form})
class FeedListView(LoginRequiredMixin,ListView):
    model=Feedback
    context_object_name='feed'
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['feed']=context['feed'].filter(user=self.request.user)
         return context
@login_required(login_url='/login')
def display(request):
    return render(request,'app/display.html')