from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "december",
}

def index(request):
    list_items = list(challenges.keys())
    li_list = ""
    for item in list_items:
        capitalized = item.capitalize()
        month_path = reverse("monthly_challenge", args=[item])
        li_list += f'<li><a href="{month_path}">{capitalized}</a></li>'

    response_data = f'<ul>{li_list}</ul>'

    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirected_month = months[month - 1]
    redirected_path = reverse('monthly_challenge', args=[redirected_month])

    return HttpResponseRedirect('/challenges/' + redirected_path)
