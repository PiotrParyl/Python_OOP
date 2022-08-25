from asyncio.windows_events import NULL
from models import Player, items
import db 
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db.engine)
session = Session()


players_list = []

def test_function():
    new_player = db.player_info('elf',3,4,2,'pusto','pusto',3,2,'Fajny łuk')
    session.add(new_player)
    session.commit()


def create_player():
    
    while True:
        print("---Create Player---")
        name = input("Name: ")
        str = input('Strenght: ')
        str = int(str)
        mgp = input('Magickpower: ')
        mgp = int(mgp)
        gold = input('Gold: ')
        gold = int(gold)
        health = input('Health: ')
        health = int(health)
        fate = input('Fate: ')
        fate = int(fate)
        special_abilities = input('Special Abilities: ')
        print("---Your Character---")
        print(f"Name: {name}\n Str:{str} \n Mgp={mgp} \n Gold = {gold} \n  Health = {health} \n Fate = {fate} \n Special Abilities = {special_abilities} \n Every thin is ok ? (y/n)")
        anser = input("-->")

        if anser == 'y':
            #new_player = Player(name,str,mgp,gold,health,fate,special_abilities)
            add_player = db.player_info(name,str,mgp,gold,"","",health,fate,special_abilities)
            session.add(add_player)
            session.commit()


            break
        if anser == 'n':
            continue



#================================================= Działająca funkcja, ale trzeba dodać while, jak chłop źle coś wpisze to misi być error dla użytkownika


def describle_player():
    print("---Describle Player---")
    print('-Wich one:')
    for obj in session.query(db.player_info).all():
        print(obj.name,)
    
    anser = input("-->")

    for obj in session.query(db.player_info).filter(db.player_info.name == anser):
        if anser == obj.name:
            print("-------------------------------------")
            print(f"Name: {obj.name}")
            print(f"Str: {obj.str}")
            print(f"Mgp: {obj.mgp}")
            print(f"Gold: {obj.gold}")
            print(f"Items: {obj.items}")
            print(f"Friends: {obj.friends}")
            print(f"HP: {obj.hp}")
            print(f"Fate: {obj.fate}")
            print(f"Abilities: {obj.abilities}")
            print("-------------------------------------")


     


#================================================= Praaaaaawie działająca funkcja edycji Playera, jeszcze trzeba co nieco pomyśleć. 

def edit_player():
    print("---Edit Player Parametr---")
    print('-Wich one parametr edit:')
    for obj in players_list:
        print("-------------------------------------")
        print(f"Name: {obj.name} (1)")
        print(f"Str: {obj.strenght} (2)")
        print(f"Mgp: {obj.magickpower} (3)")
        print(f"Gold: {obj.gold} (4)")
        print(f"Items: {obj.items} (5)")
        print(f"Friends: {obj.friends} (6)")
        print(f"HP: {obj.health} (7)")
        print(f"Fate: {obj.fate} (8)")
        print(f"Abilities: {obj.special_abilities} (9)")
        print("-------------------------------------")

        anser = input("--->")
        
        if anser == "1":
            new_name = input("New Name:")
            players_list[0].name = new_name
            continue
        if anser == "2":
            pass
        if anser == "3":
            pass
        if anser == "4":
            pass
        if anser == "5":
            pass
        if anser == "6":
            pass
        if anser == "7":
            pass
        if anser == "8":
            pass
        if anser == "9":
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
        if anser == '3':
            edit_player()





if __name__=="__main__":
    run_menu()