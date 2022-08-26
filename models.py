


class Item:

    def __init__(self,type,cost,):
        pass

#================================================= classa Player, fajnie, ale trzeba dodać funkcje del (gdy stracimy wszystkie punkty życia), tak zwany dekonstruktor, i inne ale to potem 
 
class Player:

    def __init__(self,name,strenght,magickpower,gold,health,fate,special_abilities):
        self.name = name
        self.strenght = strenght
        self.magickpower = magickpower
        self.gold = gold
        self.items = None
        self.friends = None
        self.health = health
        self.fate = fate
        self.special_abilities = special_abilities




    def edit_items(self):
        pass

    def edit_skils(self):
        pass

