from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": None,
}

def index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {"months": months})



def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text,
        })
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirected_month = months[month - 1]
    redirected_path = reverse('monthly_challenge', args=[redirected_month])

    return HttpResponseRedirect('/challenges/' + redirected_path)
