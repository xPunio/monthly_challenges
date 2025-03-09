from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


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
    "december": "december",
}


def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge_by_number(request, month):
    months = challenges.keys()
    return HttpResponse
