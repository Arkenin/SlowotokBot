from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

from bot.utils import Solver

solver = Solver()

class LettersForm(forms.Form):
    letters = forms.CharField(label="Enter your letters")

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