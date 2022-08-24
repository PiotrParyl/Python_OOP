




items = {
    'weapon':{
        'swords':{
            'sword1':{
                'str':5,
                'dps': 10,
                'cost':1,
                'lvl':3,
            },
            'sword2':{
                'str':8,
                'dps': 20,
                'cost':5,
                'lvl':7,
            },
        },
        'axes':{
            'axe1':{
                'str':6,
                'dps': 13,
                'cost':2,
                'lvl':4,
                },
            'axe2':{
                'str':10,
                'dps': 24,
                'cost':6,
                'lvl':6,
                },
        },
    },
    'armors':{
        'helms':{
            'helm1':{
                'str':4,
                'armor': 5,
                'cost':1,
                'lvl':2,
                },
            'helm2':{
                'str':6,
                'armor': 8,
                'cost':3,
                'lvl':5,
            },
        },
        'gloveses':{
            'gloves1':{
                'str':2,
                'armor': 3,
                'cost':2,
                'lvl':1,
            },
            'gloves2':{
                'str':4,
                'armor': 6,
                'cost':3,
                'lvl':4,
            },
        },
    },
}


class Item:

    def __init__(self,type,cost,):
        pass



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

