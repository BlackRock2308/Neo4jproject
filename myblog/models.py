from django.db import models
from py2neo import Graph


graph = Graph("bolt://localhost:7687", auth=("mbaye30", "mbayesene30"), name="myneo4jdb")

# Create your models here.

def get_all_users():
    query = '''
    MATCH (n:User) RETURN n
    '''
    return graph.run(query)

def count_all_users():
    query = '''
    MATCH (m:User) 
    RETURN count(m)
    '''
    return graph.run(query)

def get_all_actors():
    query = '''
    MATCH (p:Person) RETURN p LIMIT 10
    '''
    return graph.run(query)

def get_all_movies():
    query = '''
    MATCH (m:Movie) RETURN m LIMIT 8
    '''
    return graph.run(query)

def count_all_actors():
    query = '''
    MATCH (n:Person) 
    RETURN count(n)
    '''
    return graph.run(query)

def count_all_movies():
    query = '''
    MATCH (m:Movie) 
    RETURN count(m)
    '''
    return graph.run(query)

def get_all_articles():
    query =  '''
    MATCH (a:Article)
    RETURN a
    '''
    return graph.run(query)
