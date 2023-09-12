def qualif(genre,temps, champion):
    """Fonction qui vérifie si un atlète est qualifié

    Args:
    temps (int) : le temps du joueur
    champion (bool) : Etre championn du monde
    genre (str) : genre du joueur
    """    
    if genre == "homme" and temps < 12 or champion:
        return True
    if genre == "femme" and temps < 15 or champion:
        return True
    return False



def contravention(depassement_vitesse, vitesse_zone, recidive):
    """Fonction qui donne les sanctions encourues par un automobiliste en fonction de son dépassement en entrée.

    Args:
        depassement_vitesse (int): Vitesse de dépassement
    """   
    if depassement_vitesse == 20:
        if vitesse_zone > 50:
            return(68,1,0)
        else:
            return(135,1,0)
    if depassement_vitesse > 20 and depassement_vitesse <= 30:
        return(135,2,0)
    if depassement_vitesse > 30 and depassement_vitesse <= 40:
        return(135,3,3)
    if depassement_vitesse > 40 and depassement_vitesse <= 50:
        return(135,4,3)
    if depassement_vitesse > 50:
        if recidive:
            return(3750,6,3,3)
        else:
            return(1500,6,3)
    
    