def syracuse_l(n):
    """
    Calcule la suite de Syracuse à partir d'un entier n.
    
    Args:
        n (int): L'entier de départ de la suite de Syracuse.
    
    Returns:
        list: La liste contenant les valeurs de la suite de Syracuse.
    """
    l = [n]

    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int((n * 3) + 1)
        l.append(n)

    return l


def temps_de_vol(l):
    """
    Retourne le temps de vol, qui correspond au nombre d'étapes
    de la suite de Syracuse jusqu'à atteindre 1.
    
    Args:
        l (list): La liste de la suite de Syracuse.
    
    Returns:
        int: Le nombre d'étapes (temps de vol).
    """
    return len(l)


def temps_de_vol_en_altitude(l):
    """
    Calcule le temps de vol en altitude, c'est-à-dire le nombre
    d'étapes avant que la valeur ne soit inférieure à la valeur initiale.
    
    Args:
        l (list): La liste de la suite de Syracuse.
    
    Returns:
        int: Le nombre d'étapes avant de redescendre en dessous de la valeur initiale.
    """
    origin = l[0]
    n = 1

    if len(l) > 3:
        for p in range(len(l)):
            if origin > l[p]:
                return p
    return n


def altitude_maximale(l):
    """
    Retourne l'altitude maximale atteinte par la suite de Syracuse,
    c'est-à-dire la plus grande valeur de la liste.
    
    Args:
        l (list): La liste de la suite de Syracuse.
    
    Returns:
        int: L'altitude maximale (plus grande valeur de la suite).
    """
    n = 0
    for i in l:
        if i > n:
            n = i
    return n