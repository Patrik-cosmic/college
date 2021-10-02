from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
import datetime
# Create your views here.
def index(request):
    # res = Quote.objects.all()
    # print(type(res[0]))
    # print(type(res[1]))

    # for quotes in res:
    #     print(quotes.content)

    # return HttpResponse("Welcome to CTCJ college")
    context = {
        'data': Quote.objects.all(),
        'comment_date': datetime.date.today(),
    }
    return render(request, 'college/home.html', context=context)