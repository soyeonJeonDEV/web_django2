from django.shortcuts import render

from .api import check_covid,mail
from django.core.cache import cache 

def index(request):
    data = check_covid()
#    cache_data = cache.get("covid_data")
    num = []
#    if cache_data is None:
    mail_data = mail()
    for number in mail_data['tr']['td']:
        num.append(number['span'])
#        num = cache.set("covid_data", num , timeout=600 * 600)

    return render(request, 'covid_checker/covid_main.html',{'data':data,'today':num})
        
# Create your views here.
