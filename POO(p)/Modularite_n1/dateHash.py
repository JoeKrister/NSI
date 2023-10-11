# Module utilisant un tableau de hashage

def cree():
    return [[] for _ in range(23)]

def contient(data,s):
    return data in s[data%23]

def ajoute(data,s) :
    s[data%23].append(data)
    