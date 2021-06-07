from django.shortcuts import render

from .models import * 
# Create your views here.



def home(request):
    users = get_all_users()
    persons = get_all_actors()
    movies = get_all_movies()
    nombre_actors = count_all_actors()
    nombre_users = count_all_users()
    print(nombre_users)
    nombre_movies = count_all_movies()
    context = {'users':users,'nombre_users':nombre_users,'persons' : persons, 'movies' : movies, 'nombre_actors':nombre_actors, 'nombre_movies':nombre_movies}
    
    return render(request, "myblog/dashboard.html", context)


def get_article(request):
    articles = get_all_articles()
    context = {"articles":articles}
    return render(request,"myblog/post.html", context) #post.html



def post_detail(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    context = {}
    return render(request, "myblog/post_details.html", context)

def writearticle(request):
    context = {}
    return render(request, "myblog/writepost.html", context)