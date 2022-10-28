from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
# Create your views here.
def feedback(request):
    form=FeedbackForm()
    return render(request,'app/feedback.html',{"form":form})