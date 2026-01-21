from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.contrib.auth.decorators import login_required

@login_required
def person_form_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save() # Saves the valid data to the database
            return redirect(request.path) # Redirect back to the same form (POST-Redirect-GET)
    else:
        form = PersonForm() # Create a new, blank form for a GET request
    
    # Pass existing data to the template to display a list of saved records
    people = Person.objects.all() 
    return render(request, 'userForm/person_form.html', {'form': form, 'people': people})
