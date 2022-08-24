from models import Player, items





players_list = []





def create_player():
    
    while True:
        print("---Create Player---")
        name = input("Name: ")
        str = input('Strenght: ')
        mgp = input('Magickpower: ')
        gold = input('Gold: ')
        
        
        health = input('Health: ')
        fate = input('Fate: ')
        special_abilities = input('Special Abilities: ')
        print("---Your Character---")
        print(f"Name: {name}\n Str:{str} \n Mgp={mgp} \n Gold = {gold} \n  Health = {health} \n Fate = {fate} \n Special Abilities = {special_abilities} \n Every thin is ok ? (y/n)")
        anser = input("-->")

        if anser == 'y':
            new_player = Player(name,str,mgp,gold,health,fate,special_abilities)
            players_list.append(new_player)
            break
        if anser == 'n':
            continue



def describle_player():
    print("---Describle Player---")
    
    for obj in players_list:
        print(f"Name: {obj.name}")
        print(f"Str: {obj.strenght}")
        print(f"Mgp: {obj.magickpower}")
        print(f"Gold: {obj.gold}")
        print(f"Items: {obj.items}")
        print(f"Friends: {obj.friends}")
        print(f"HP: {obj.health}")
        print(f"Fate: {obj.fate}")
        print(f"Abilities: {obj.special_abilities}")
        print("-------------------------------------")
    
       


def edit_player(player):
    pass


def print_Player():
    pass

def run_menu():

    while True:
        print("---Player Infro---")
        print("-Create Player: (1)")
        print("-Describle Player: (2)")
        print("-Edit Player: (3)")
        print("-Exit: (q)")
        anser = input("-->")

        if anser == '1':
            create_player()
        if anser == '2':
            describle_player()






if __name__=="__main__":
   pass