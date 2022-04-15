from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

from bot.utils import Solver
from .models import User

solver = Solver()

class LettersForm(forms.Form):
    letters = forms.CharField(label = '')

def results(request):
    return render(request, "bot/results.html", {
        "letters": request.session["letters"],
        "words": request.session["words"],
    })

def greet(request, name):
    return render(request, "bot/index.html", {
        "name": name.capitalize()
    })

def index(request):

    if "letters" not in request.session:

        request.session["letters"] = None

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = LettersForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["letters"]
            # run some code
            out = task.lower()
            words = set(solver.solve(out))
            request.session["letters"] = out
            request.session["words"] = sorted(words, key=len, reverse=True)

            # Redirect user to list of words
            return HttpResponseRedirect(reverse("results"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "bot/index.html", {
                "form": LettersForm
            })

    return render(request, "bot/index.html", {
        "form": LettersForm(),
        "letters": request.session["letters"],
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bot/login.html", {
                "message": "Nieprawodłowy login lub hasło."
            })
    else:
        return render(request, "bot/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "bot/register.html", {
                "message": "Hasła muszą się zgadzać."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "bot/register.html", {
                "message": "Nazwa użytkownika zajęta."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "bot/register.html")