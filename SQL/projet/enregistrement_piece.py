
def ajouter():
    piece = {}
    while True:
        nb = input('Numéro de la pièce ?')
        if nb == 's':
            return piece
        else:
            ex = input("nombre d'exemplaire ?")
            piece[nb] = ex
        
