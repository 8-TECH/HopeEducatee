from django.shortcuts import render
from .models import School  # Assuming your model is named School

def school_view(request):  # Changed function name to avoid conflict with model
    schools = School.objects.all()  # Fetch all updates

    context = {'school': schools}  # Use 'schools' here to match the queried data
    return render(request, 'School/school.html', context)
