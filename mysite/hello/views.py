from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View

def cookie(request):
    print(request.COOKIES)

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del(request.session['num_visits'])
    resp = HttpResponse('view count=' + str(num_visits))

    resp.set_cookie('hamadaCookie', 42, max_age=1000) # seconds till expiry
    resp.set_cookie('dj4e_cookie', 'e12adf20', max_age=1000)
    return resp