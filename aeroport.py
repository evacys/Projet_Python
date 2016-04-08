'''
Created on 6 avr. 2016

@author: eleve
'''
class Aeroport(object):
    def __init__(self,identifiant,nom,ville,lat,long):
        """
        Constructeur de la classe Aeroport
        
        Parametres:
        lat = latitude
        long = longitude
        """
        self.id = identifiant
        self.nom = nom
        self.ville = ville
        self.lat = lat
        self.long = long
        
