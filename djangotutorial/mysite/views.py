from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods


def apps_index(request):
    """Show a list of installed non-Django apps and link to their mounted URL paths.

    This extracts the top-level package name from each entry in
    settings.INSTALLED_APPS and filters out Django contrib/system apps.
    It then links to '/<app>/' which matches the common pattern of
    mounting an app at that path (for example, the 'polls' app is
    mounted at '/polls/').
    """
    apps = []
    for entry in settings.INSTALLED_APPS:
        # ignore Django-provided packages
        if entry.startswith("django."):
            continue
        # extract base app label (e.g. 'polls' from 'polls.apps.PollsConfig')
        app_label = entry.split(".")[0]
        if app_label == "mysite":
            continue
        if app_label not in apps:
            apps.append(app_label)

    return render(request, "index.html", {"apps": apps})


@require_http_methods(["GET", "POST"])
def register(request):
    """Simple user registration view using Django's built-in UserCreationForm.

    On successful registration the user will be logged in and redirected
    to the site root.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in and redirect to the index
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})
