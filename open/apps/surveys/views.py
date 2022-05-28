from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from apps.surveys.models import Survey
from apps.surveys.forms import SurveyForm

def index(request):
    return render(request, "surveys/index.html")

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    form = SurveyForm(survey)
    
    context = {
      "survey": survey,
      "form": form,
    }
    return render(request, "surveys/survey.html", context)