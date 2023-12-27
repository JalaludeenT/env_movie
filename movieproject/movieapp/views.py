from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm


# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def details(request, movie_id):
    movies = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'Movies': movies})
    # return HttpResponse("This is a movie %s" % movie_id)


def add_movie(request):
    if request.method == 'POST':
        movie_name = request.POST.get('Name')
        movie_Desc = request.POST.get('Description')
        movie_Year = request.POST.get('Year')
        movie_img = request.FILES['Images']
        add_all_movie = Movie(Name=movie_name, Description=movie_Desc, Year=movie_Year, Images=movie_img)
        add_all_movie.save()
    return render(request, 'add.html')


def update(request, id):
    u_movie = Movie.objects.get(id=id)
    u_form = MovieForm(request.POST or None, request.FILES, instance=u_movie)
    if u_form.is_valid():
        u_form.save()
        return redirect('/')
    return render(request, 'edit.html', {'Form': u_form, 'movie': u_movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')

