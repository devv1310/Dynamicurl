from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def integer(request, pk, id, pkid, idpk):
    data = {
        "data1": pk,
        "data2": id,
        "data3": pkid,
        "data4": idpk,
    }
    return render(request, 'home.html', {'key': data})
