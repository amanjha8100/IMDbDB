from django.shortcuts import render
from . models import Directors,Movies
# Create your views here.
def index(request):
    movies = Movies.objects.all()
    mcount = Movies.objects.all().count()
    context = {
        'movies':movies,
        'mc':mcount,
    }
    return render(request,'filter/movies.html',context)

def movie(request):
    movies = Movies.objects.all()
    mcount = Movies.objects.all().count()
    context = {
        'movies':movies,
        'mc':mcount,
    }
    return render(request,'filter/movies.html',context)


# def filter(request):
    qs1 = Directors.objects.all()
    qs2 = Movies.objects.all()
    qsn = list()
    qdirector = list()
    directorq = request.GET.get('name')
    mtitleq = request.GET.get('original_title')
    muidq = request.GET.get('uid')
    mratingq = request.GET.get('vote_average')
    if directorq != '' and directorq is not None:
        qs1 = qs1.filter(name__startswith=directorq)
        x = qs1.values_list(directors__name)
        print(qs1)
        # qs2 = qs2.filter(director_id=)
        qs1c = qs1.count()
        for q in qs1:
            mfilter = qs2.filter(director_id=q.uid)
            mfilterc = mfilter.count()
            for i in range(0,mfilterc):
                qdirector.append(q.name)
            qsn += mfilter
            print(len(qsn))
        print(qdirector)
        print(len(qsn))
    context = {
        'qs1':qs1,
        'qsn':qsn,
        'qs2':qs2,
        'qdirector':qdirector,
    }   
    return render(request,'filter/filterform.html', context)

def filter(request):
    context = {
        
    }   
    return render(request,'filter/filterform.html', context)

def util():
    pass
