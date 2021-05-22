from django.shortcuts import render
from . models import Directors,Movies
# Create your views here.
def index(request):
    directors = Directors.objects.all();
    dc = directors.count()
    context = {
        'directors':directors,
        'dc':dc,
    }
    return render(request,'filter/index.html',context)

def movie(request):
    movies = Movies.objects.all()
    mcount = Movies.objects.all().count()
    context = {
        'movies':movies,
        'mc':mcount,
    }
    return render(request,'filter/movies.html',context)


def filter(request):
    qs2 = Movies.objects.all()
    mtitleq = request.GET.get('original_title')
    muidq = request.GET.get('uid')
    mratingq = request.GET.get('vote_average')
    votecountq = request.GET.get('vote_count')
    budgetq = request.GET.get('budget')
    releasedfrom = request.GET.get('release_date_from')
    releasedto = request.GET.get('release_date_to')
    if mtitleq != '' and mtitleq is not None:
        qs2 = qs2.filter(original_title__startswith=mtitleq)
    if muidq != '' and muidq is not None:
        qs2 = qs2.filter(uid=muidq)
    if mratingq != '' and mratingq is not None:
        qs2 = qs2.filter(vote_average__gte=mratingq)
    if votecountq != '' and votecountq is not None:
        qs2 = qs2.filter(vote_count__gte=votecountq)
    if budgetq != '' and budgetq is not None:
        qs2 = qs2.filter(budget__gte=budgetq)
    if releasedfrom != '' and releasedfrom is not None:
        qs2 = qs2.filter(release_date__gte=releasedfrom)
    if releasedto != '' and releasedto is not None:
        qs2 = qs2.filter(release_date__lt=releasedto)
    context = {
        'qs2':qs2,
        'qc':qs2.count(),
    }
    return render(request,'filter/filterform.html', context)

def filterD(request):
    qs = Directors.objects.all()
    query = request.GET.get('name')
    if query != '' and query is not None:
        qs = qs.filter(name__startswith=query)
    context={
        'qs':qs,
        'qc':qs.count(),
    }
    return render(request,'filter/filterD.html',context)

# def dmovie(request, uid):

