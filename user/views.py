from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from py2neo import Graph, Node, Relationship,NodeMatcher

# from datetime import datetime
from passlib.hash import bcrypt
from .models import *
from django.contrib import messages


graph = Graph("bolt://localhost:7687", auth=("mbaye30", "mbayesene30"), name="myneo4jdb")

def accueil(request):
    user=request.user
    
    matcher = NodeMatcher(graph)
    queryf = "match ((n {username:$username})-[f:Follows]->(p:Utilisateur)) return p.username"
    a=user.username
    followers=graph.run(queryf, parameters={'username': user.username}).to_table()
    print(followers)
    context={

        'followers':followers,
        
    }
    return render(request,'user/accueil.html',context)
    

def myLogin(request):
    if request.method == "POST":
        username  = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if (username == 'mbayemc2'):
                return redirect('dashboard')
            else:
                return redirect('accueil')
        else:
            messages.error(request,"Le mot de pass et le nom d'utilisateur ne correspondent pas")

    return render(request,'user/login.html')


def register(request):
    tx=graph.begin()
    if request.method == "POST":
        username=request.POST['username']
        prenom=request.POST['prenom']
        nom=request.POST['nom']
        mail=request.POST['email']
        password = request.POST['password']

        user = User()
        user.first_name=prenom
        user.last_name=nom
        user.set_password(password)
        user.username = username
        user.email=mail

        
        tx.run("CREATE (person:Utilisateur{username:$name,password:$password}) Return person",name=username,password=bcrypt.encrypt(password))
        graph.commit(tx)
        user.save()
        return redirect ('accueil')
    return render(request,'user/register.html')


@login_required
def profile(request):
    user=request.user
    # matcher = NodeMatcher(graph)
    # query = 'match (n:Utilisateur) where n.username={user.username} return ID(n)'
    # utilisateur = matcher.match("User", username=user.username)
    # id_user = graph.run(query, parameters={'username': user.username}).evaluate()

    context = {
        'user': user,

    }
    return render(request,'user/profile.html',context)



def myLogout(request):
    logout(request)
    return redirect('accueil')


