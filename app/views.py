from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg="hello friends very very"
    h=int(date.strftime('%H'))
    if h<12:
        msg+='Goodmorning'
    elif h<16:
        msg+='Good afternoon'
    elif h<21:
        msg+="good evening"
    else:
        msg+='good night'
    d={'insert_date':date,'insert_msg':msg}
    return render(request,'first.html',d)