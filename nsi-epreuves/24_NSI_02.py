def correspond(mot : str, mot_a_trous : str)-> bool:
    assert type(mot) == str, "Erreur sur type"
    assert type(mot_a_trous) == str, "Erreur sur type"
    if len(mot) != len(mot_a_trous):
        return False
    else:
        for i in range(len(mot)):
            if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
                return False
        return True
                    
            
        
        
    


