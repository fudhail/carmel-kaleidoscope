from django.shortcuts import render
from django.http import HttpResponse
from account.models import User
from django.db.models import Q


def HomePage(request):
    def get_client_ip(request):
     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
     if x_forwarded_for:
         ip = x_forwarded_for.split(',')[0]
     else:
         ip = request.META.get('REMOTE_ADDR')
     return ip
    ip=get_client_ip(request)
    u=User(user=ip)
    result=User.objects.filter(Q(user__icontains=ip))
    if len(result)==1:
        print('exists')
    else:
        u.save()
        print('unique')
    count=User.objects.all().count()
    return render(request, 'home/index.html',{'count':count})
