from django.shortcuts import render,redirect
from django.core.mail import send_mass_mail,BadHeaderError
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Feedback
from django.http import HttpResponse
from django.db.models import Count
from .forms import FeedbackForm
# Create your views here.
@login_required(login_url='/login')
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            rating = form.cleaned_data['rating']
            email = form.cleaned_data['email']
            comments = form.cleaned_data['comments']

            k = form.save(commit=False)
            k.user = request.user
            k.save()

            try:
                m1 = (
                    f"Feedback Form By {k.user}",
                    f"Subject: {subject}\nRating: {rating}\nFeedback: {comments}",
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                m2 = (
                    "Thank you for your response",
                    "Please keep giving regular feedback",
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                send_mass_mail((m1, m2), fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            
            return redirect('/feed')
    else:
        form = FeedbackForm()
    
    return render(request, 'app/feedback.html', {"form": form})
class FeedListView(LoginRequiredMixin,ListView):
    model = Feedback
    context_object_name = 'feed'
    template_name = 'feedback_list.html' 

    def get_queryset(self):
        return Feedback.objects.filter(user=self.request.user).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ratings = self.get_queryset().values_list('rating', flat=True)

        feedbacks_count = (
            Feedback.objects
            .values('user')
            .annotate(count=Count('id'))
            .order_by('-count')
        )

        labels = ['1⭐', '2⭐', '3⭐', '4⭐', '5⭐']
        ratings_data = [ratings.filter(rating=i).count() for i in range(1, 6)]

        context['ratings'] = ratings
        context['labels'] = labels
        context['ratings_data'] = ratings_data
        context['feedbacks_count'] = feedbacks_count

        return context
    
@login_required(login_url='/login')
def display(request):
    return render(request,'app/display.html')

