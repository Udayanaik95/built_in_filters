from django.shortcuts import render

# Create your views here.

def built_in_filter(request):
    import datetime
    dt='ThiS iS My fiRsT Page'
    ds=datetime.datetime.now()
    d={'dt':dt,'ds':ds}
    return render(request,'built_in_filter.html',d)
