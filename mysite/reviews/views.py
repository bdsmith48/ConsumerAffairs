from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from .models import Review
from . import forms
import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        latest_review_list = Review.objects.filter(reviewer_name=request.user.username).order_by('-submission_date')
        template = loader.get_template('reviews/index.html')
        context = {
            'latest_review_list': latest_review_list,
        }
        return HttpResponse(template.render(context, request))

def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/detail.html', {'review': review})

def write_review(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            r_name = request.user.get_username()
            form = forms.WriteReviewForm(request.POST)
            if form.is_valid():
                int_rating = models.Review(rating = form.cleaned_data['rating'], title = form.cleaned_data['title'], summary = form.cleaned_data['summary'], company = form.cleaned_data['company'], reviewer_name = r_name)
                int_rating.save()
                context = {"form": form}
                return HttpResponseRedirect("index")
        else:
            form = forms.WriteReviewForm()
            context = {"form": form}
            return render(request, 'reviews/writeReviews.html', context)
    else:
        return redirect("/login")
