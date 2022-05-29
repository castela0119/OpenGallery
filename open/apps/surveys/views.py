from django.shortcuts import get_object_or_404
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt


from apps.surveys.models import Survey, Submission
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

# @csrf_exempt
# def otp_callback(request):
#     data = json.loads(request.body)
#     submission_id = int(data["metadata"])
#     email = data["email"]
#     auth_status = data["auth_status"]

#     submission = get_object_or_404(Submission, pk=submission_id, participant_email=email)
#     submission.status = auth_status
#     submission.save()
#     return HttpResponse("OK")